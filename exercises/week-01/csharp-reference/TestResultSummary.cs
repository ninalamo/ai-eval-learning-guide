// Reference sketch — do not compile this. Port the behavior to src/summarize.py.
// Maps: record → dataclass, Path → pathlib, using → context manager.

using System.Text.Json;

public sealed record TestResult(
    string Name,
    string Status, // "passed" | "failed" | "skipped"
    string? Tag,
    int DurationMs);

public sealed record Summary(
    int Total,
    int Passed,
    int Failed,
    IReadOnlyDictionary<string, double> PassRateByTag);

public static class TestResultSummary
{
    public static IReadOnlyList<TestResult> LoadResults(string path)
    {
        var json = File.ReadAllText(path);
        return JsonSerializer.Deserialize<List<TestResult>>(json)
               ?? throw new InvalidOperationException("results json was null");
    }

    public static Summary Summarize(IReadOnlyList<TestResult> results)
    {
        var passed = results.Count(r => r.Status == "passed");
        var failed = results.Count(r => r.Status == "failed");
        return new Summary(results.Count, passed, failed, PassRateByTag(results));
    }

    public static IReadOnlyDictionary<string, double> PassRateByTag(
        IReadOnlyList<TestResult> results)
    {
        // Skipped rows are omitted from the denominator.
        // Untagged rows are omitted from the map (they still count in Total).
        return results
            .Where(r => r.Tag is not null && r.Status is "passed" or "failed")
            .GroupBy(r => r.Tag!)
            .ToDictionary(
                g => g.Key,
                g => g.Count(r => r.Status == "passed") / (double)g.Count());
    }
}
