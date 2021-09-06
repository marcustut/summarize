export const isWord = (text: string): boolean => {
  const arr = text.split("").map((c) => {
    let code = c.charCodeAt(0);
    return (
      (code > 47 && code < 58) || // numeric (0-9)
      (code > 64 && code < 91) || // upper alpha (A-Z)
      (code > 96 && code < 123) // lower alpha (a-z)
    );
  });
  return arr[0];
};

export const wordCounter = (text: string): number => {
  let count = 0;
  text.split(" ").forEach((word) => word !== " " && isWord(word) && count++);
  return count;
};
