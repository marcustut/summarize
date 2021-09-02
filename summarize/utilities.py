from typing import List

# Used by models using HuggingFace pipeline functions to
# To convert a returned summary of type List["dict[str str]"] to a concatenated string
def append(raw_summary: List) -> str:
    for d in raw_summary:
        summary = "".join(str(val.capitalize()) + "\n" for _, val in d.items())

        # Remove extra spaces
        summary = summary.replace(" .", ".")
        summary = summary.replace(" !", "!")
        summary = summary.replace(" ?", "?")
        return summary
