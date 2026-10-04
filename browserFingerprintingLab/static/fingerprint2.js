(() => {
  const target = document.getElementById("target-sentence").textContent;
  const input = document.getElementById("typing-input");
  const output = document.getElementById("typing-results");
  const restart = document.getElementById("restart");
  let start = null;
  let corrections = 0;
  let finished = false;
  // Curly apostrophes are awkward to enter on some keyboards. Accept the
  // straight apostrophe as the same visible punctuation for the comparison.
  const normalizeSentence = (text) => text.replace(/[\u2018\u2019]/g, "'");

  input.addEventListener("keydown", (event) => {
    if (finished) return;
    if (start === null && event.key.length === 1) start = performance.now();
    if (event.key === "Backspace" && !event.repeat && input.value.length > 0) {
      corrections += 1;
    }
  });

  input.addEventListener("input", async () => {
    if (finished || start === null || normalizeSentence(input.value) !== normalizeSentence(target)) return;
    finished = true;
    const elapsedSeconds = (performance.now() - start) / 1000;
    const charactersPerMinute = target.length * 60 / elapsedSeconds;
    const wordsPerMinute = charactersPerMinute / 5;
    const result = {
      task: "typing",
      character_count: target.length,
      typing_time: elapsedSeconds,
      typing_speed_cpm: charactersPerMinute,
      typing_speed_wpm: wordsPerMinute,
      correction_count: corrections,
    };
    output.textContent = `Typing time: ${elapsedSeconds.toFixed(2)} s\n` +
      `Typing speed: ${charactersPerMinute.toFixed(2)} characters/min ` +
      `(${wordsPerMinute.toFixed(2)} words/min)\n` +
      `Backspace corrections: ${corrections}\nSending results to Flask…`;
    try {
      const response = await fetch("/collect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(result),
      });
      const confirmation = await response.json();
      output.textContent = `Typing time: ${elapsedSeconds.toFixed(2)} s\n` +
        `Typing speed: ${charactersPerMinute.toFixed(2)} characters/min ` +
        `(${wordsPerMinute.toFixed(2)} words/min)\n` +
        `Backspace corrections: ${corrections}\n` +
        `${confirmation.status} (HTTP ${response.status})`;
    } catch (error) {
      output.textContent += `\nSend failed: ${error.message}`;
    }
  });

  restart.addEventListener("click", () => {
    input.value = "";
    start = null;
    corrections = 0;
    finished = false;
    output.textContent = "";
    input.focus();
  });

})();
