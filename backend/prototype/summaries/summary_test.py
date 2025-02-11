import timeit
from bart_summary import bartSummary
from gemini_summary import geminiSummary
from t5_summary import tFiveSummary

# For each function, run 10 tests and take the average time
def test(text):
    functions = [bartSummary, geminiSummary, tFiveSummary]
    results = {}

    for func in functions:
        execution_time = timeit.timeit(lambda: func(text, False), number=10)
        results[func.__name__] = execution_time / 10

    return results

# Main func that has example text and calls the summarization test file
if __name__ == "__main__":
    text = """
    Good morning, everyone. Let's get started. First on the agenda, the marketing team has been working on the new campaign, and Sarah, could you give us a quick update?
    Sure! We've finalized the designs, and the content is almost ready. We expect to launch by the end of next week.
    Great! Next, the development team. John, how's the progress on the new feature?
    We're about 80% done. We still need to finalize testing, but everything looks good so far.
    Awesome. Let's aim for a final review by Friday. Does that timeline work for everyone?
    Yes, that should be fine.
    Perfect. Finally, on operations, we’ve been getting some customer feedback about response times. Lisa, can you look into that?
    Yes, I'll analyze the data and propose some improvements by the next meeting.
    Sounds good. Any other topics before we wrap up?
    Nope, that covers everything.
    Alright, thanks, everyone! See you next week.
    """

    results = test(text)

    # Print results
    # Last execution:
    # bartSummary: 9.101945 seconds per execution
    # geminiSummary: 1.163149 seconds per execution
    # tFiveSummary: 11.885445 seconds per execution
    for name, time_taken in results.items():
        print(f"{name}: {time_taken:.6f} seconds per execution")