"""Deck-derived content for the Evaluation and Experiment Tracker Explainer."""

PAGES = [
    {
        "id": 1,
        "title": "Evaluation Metrics",
        "short_title": "Metrics",
        "page": "pages/01_evaluation_metrics.py",
        "icon": ":material/analytics:",
        "deck_source": "Slide 1",
        "why_it_matters": (
            "Traditional metrics are still useful, but production AI systems need more than "
            "historical test-set scores. A system can have a strong benchmark score and still "
            "fail because it is slow, expensive, inconsistent, or brittle when inputs change."
        ),
        "concept": (
            "Metrics summarize behavior into numbers. Accuracy, RMSE, cross-validation, "
            "precision, and recall each answer a specific question about model performance. "
            "The trap is treating one number as the whole story."
        ),
        "mental_model": (
            "Think of metrics as dashboard gauges. A speedometer is useful, but it does not "
            "tell you whether you are heading toward the right destination, whether the engine "
            "is overheating, or whether the ride is comfortable."
        ),
        "common_pitfall": (
            "Do not celebrate a single high metric before asking what it ignores. For example, "
            "accuracy can hide poor recall, and a low RMSE can still hide expensive failures on "
            "the examples users care about most."
        ),
        "real_work": (
            "In practice, teams usually report a small bundle of metrics: one quality metric, "
            "one reliability metric, one latency metric, and one cost metric. That bundle gives "
            "a more honest view than a leaderboard-style score."
        ),
    },
    {
        "id": 2,
        "title": "What to Evaluate in AI Systems",
        "short_title": "AI Eval Criteria",
        "page": "pages/02_ai_system_evaluation.py",
        "icon": ":material/rule_settings:",
        "deck_source": "Slide 2",
        "why_it_matters": (
            "AI applications are judged by more than correctness. Users care whether the "
            "system understands the domain, follows instructions, gives coherent answers, "
            "responds quickly, and stays affordable at realistic usage levels."
        ),
        "concept": (
            "A useful AI evaluation plan separates quality into dimensions: domain capability, "
            "generation quality, instruction following, cost, and latency. Each dimension needs "
            "its own examples, scoring method, and threshold."
        ),
        "mental_model": (
            "Think of an AI system like a job candidate. You would not hire only from a single "
            "multiple-choice score. You would check domain knowledge, communication, reliability, "
            "speed, and fit for the actual job."
        ),
        "common_pitfall": (
            "Do not mix all criteria into one vague score too early. If an answer is factually "
            "right but ignores the requested JSON format, that is a different failure from a "
            "well-formatted answer that makes up facts."
        ),
        "real_work": (
            "A strong eval report separates dimensions so product, engineering, and domain "
            "experts can discuss the actual tradeoff: correctness, format compliance, user "
            "experience, speed, or cost."
        ),
    },
    {
        "id": 3,
        "title": "Designing an Evaluation Pipeline",
        "short_title": "Eval Pipeline",
        "page": "pages/03_evaluation_pipeline.py",
        "icon": ":material/schema:",
        "deck_source": "Slide 3",
        "why_it_matters": (
            "Evaluation should be designed before the application is finished. The pipeline "
            "clarifies what good means, where failures come from, and which data should be used "
            "to test changes safely."
        ),
        "concept": (
            "A strong pipeline evaluates components separately, writes a guideline before "
            "judging outputs, and chooses evaluation methods and datasets on purpose. This "
            "keeps you from treating a multi-step system as one mysterious black box."
        ),
        "mental_model": (
            "Think of the pipeline as a lab bench. Each component gets its own test, the rubric "
            "is the measuring instrument, and the eval dataset is the material you test against."
        ),
        "common_pitfall": (
            "Do not wait until the app is finished to create the eval set. If the eval data comes "
            "last, it often reflects what the system already does instead of what the system must do."
        ),
        "real_work": (
            "Teams often start with a small hand-built eval set, then add examples every time a "
            "new bug, user complaint, or edge case appears. The eval set becomes a living memory "
            "of what the system has learned to handle."
        ),
    },
    {
        "id": 4,
        "title": "Experiment Tracking",
        "short_title": "Tracking",
        "page": "pages/04_experiment_tracking.py",
        "icon": ":material/track_changes:",
        "deck_source": "Slides 4-5",
        "why_it_matters": (
            "Without tracking, experiments become memory and vibes. With tracking, you can "
            "explain what changed, compare runs, return to a known-good setup, and defend why "
            "one version should ship."
        ),
        "concept": (
            "Experiment tracking records parameters, metrics, artifacts, model versions, and "
            "notes for each run. Tools like MLflow and Weights & Biases make those runs easier "
            "to compare, share, and reproduce."
        ),
        "mental_model": (
            "Think of each experiment as a lab notebook entry. The model, prompt, retrieval "
            "settings, dataset, scores, cost, and artifacts all belong on the page."
        ),
        "common_pitfall": (
            "Do not log only the winning run. The losing runs explain the search path, prevent "
            "the team from repeating old mistakes, and make it easier to understand why a later "
            "change regressed."
        ),
        "real_work": (
            "A useful tracker lets someone answer: what changed, what improved, what got worse, "
            "what did it cost, and which artifact proves the result?"
        ),
    },
    {
        "id": 5,
        "title": "Observability and Architecture",
        "short_title": "Architecture",
        "page": "pages/05_observability_architecture.py",
        "icon": ":material/hub:",
        "deck_source": "Slides 6-7",
        "why_it_matters": (
            "Production AI systems are not just one model call. They often include retrieval, "
            "guardrails, gateways, caching, tools, and agents. Observability has to follow the "
            "request across all of those layers."
        ),
        "concept": (
            "AI engineering architecture can be viewed as layers: enhance context, add guardrails, "
            "route through a gateway, reduce latency, and use agent patterns when needed. Logs, "
            "traces, cost, latency, and quality signals cut across every layer."
        ),
        "mental_model": (
            "Think of a request as a package moving through a facility. Observability is the "
            "tracking number that tells you where it went, how long each stop took, and where it "
            "got damaged."
        ),
        "common_pitfall": (
            "Do not log only the final model response. In a multi-step AI system, the final output "
            "may be bad because retrieval failed, a guardrail blocked context, a router picked the "
            "wrong model, or a tool call returned stale data."
        ),
        "real_work": (
            "Production teams trace requests across components. A single trace should make it "
            "possible to reconstruct the path from user input to retrieval, prompt, model call, "
            "tool use, post-processing, and final response."
        ),
    },
    {
        "id": 6,
        "title": "Monitoring vs. Observability",
        "short_title": "Monitoring",
        "page": "pages/06_monitoring_vs_observability.py",
        "icon": ":material/monitor_heart:",
        "deck_source": "Slide 8",
        "why_it_matters": (
            "Monitoring tells you when a known metric is unhealthy. Observability helps you "
            "investigate new or surprising failures. AI systems need both because quality "
            "problems are often subtle."
        ),
        "concept": (
            "Monitoring watches known metrics such as latency, errors, cost, throughput, and "
            "queue depth. Observability uses traces, structured logs, quality drift signals, "
            "and user feedback to understand what happened inside the system."
        ),
        "mental_model": (
            "Monitoring is the alarm panel. Observability is the investigation kit. The alarm "
            "says something changed; the traces and logs help you discover why."
        ),
        "common_pitfall": (
            "Do not treat uptime as proof of quality. The service can be online while answers "
            "get less useful, citations drift, costs rise, or users quietly retry the same task."
        ),
        "real_work": (
            "A mature AI system combines service health metrics with product-quality signals: "
            "thumbs down, retries, abandonment, answer length drift, citation mismatch, and "
            "manual review samples."
        ),
    },
    {
        "id": 7,
        "title": "Experiment Tracker Lab",
        "short_title": "Tracker Lab",
        "page": "pages/07_tracker_lab.py",
        "icon": ":material/science:",
        "deck_source": "Implementation lab",
        "why_it_matters": (
            "The best way to understand experiment tracking is to try it. This lab lets you "
            "log small prompt or model experiments, compare their tradeoffs, and choose a run "
            "based on explicit criteria."
        ),
        "concept": (
            "A run is a record of one experiment. It should include what you changed, what you "
            "measured, what artifact was produced, and whether the result is good enough to keep."
        ),
        "mental_model": (
            "Think of the tracker as a decision memory. Weeks later, it should still explain "
            "why version B beat version A, and what you would try next."
        ),
        "common_pitfall": (
            "Do not choose the highest-quality run without checking the deployment constraints. "
            "A run that is slightly better but five times slower or more expensive may be the wrong "
            "production choice."
        ),
        "real_work": (
            "Teams usually choose a winner with constraints: minimum quality, maximum latency, "
            "maximum cost, and enough notes to explain why the run is safe to try next."
        ),
    },
]


METRIC_ROWS = [
    {
        "Metric": "Accuracy",
        "Measures": "Correct predictions divided by total predictions",
        "Good for": "Balanced classification tasks",
        "Limitation": "Misleading when classes are imbalanced",
    },
    {
        "Metric": "MSE / RMSE",
        "Measures": "Average squared error, optionally square-rooted",
        "Good for": "Regression problems",
        "Limitation": "Large errors dominate the score",
    },
    {
        "Metric": "Cross-validation",
        "Measures": "Average performance across folds",
        "Good for": "Generalization estimates",
        "Limitation": "Still historical; does not reveal production drift",
    },
    {
        "Metric": "Precision / Recall",
        "Measures": "False-positive and false-negative tradeoff",
        "Good for": "Risk-sensitive classification",
        "Limitation": "The right tradeoff depends on the problem",
    },
]


AI_EVAL_DIMENSIONS = [
    {
        "name": "Domain-Specific Capability",
        "questions": [
            "Does it answer correctly in the target domain?",
            "Does it handle terminology, context, and edge cases?",
            "Were the examples designed by people who know the domain?",
        ],
    },
    {
        "name": "Generation Quality",
        "questions": [
            "Is the response factual and grounded?",
            "Is it coherent across the full answer?",
            "Is the answer complete without being bloated?",
        ],
    },
    {
        "name": "Instruction Following",
        "questions": [
            "Does it respect the requested format?",
            "Does it follow tone, length, and persona constraints?",
            "Does it satisfy structure requirements such as JSON or bullets?",
        ],
    },
    {
        "name": "Cost and Latency",
        "questions": [
            "How long until the first token appears?",
            "What is the end-to-end response time?",
            "What does a call or session cost at expected volume?",
        ],
    },
]


PIPELINE_STEPS = [
    {
        "step": "01",
        "name": "Evaluate All Components",
        "summary": (
            "Do not evaluate only the final answer. Test retrieval quality, prompt behavior, "
            "tool calls, and output quality separately so failures can be traced."
        ),
    },
    {
        "step": "02",
        "name": "Create an Evaluation Guideline",
        "summary": (
            "Write down what good looks like before judging. Include examples of strong, weak, "
            "and borderline outputs so human or model judges apply the rubric consistently."
        ),
    },
    {
        "step": "03",
        "name": "Define Methods and Data",
        "summary": (
            "Choose exact checks, human review, model judges, or hybrid methods based on the "
            "dimension. Build an eval dataset early and update it as new failures appear."
        ),
    },
]


TRACKING_TOOLS = [
    {
        "tool": "MLflow",
        "tracks": "Parameters, metrics, artifacts, model versions, run comparisons",
        "best_for": "Traditional ML, scikit-learn, custom pipelines, self-hosted workflows",
    },
    {
        "tool": "Weights & Biases",
        "tracks": "Training curves, visualizations, shared runs, collaboration, artifacts",
        "best_for": "Deep learning, fine-tuning, Hugging Face, PyTorch, team settings",
    },
]


SAMPLE_RUNS = [
    {
        "Run": "A",
        "Model": "Fast model",
        "Prompt": "v1 direct answer",
        "Retrieval": "top_k=3",
        "Quality": 0.72,
        "Latency sec": 1.1,
        "Cost cents": 0.4,
        "Notes": "Fast and cheap, misses details.",
    },
    {
        "Run": "B",
        "Model": "Balanced model",
        "Prompt": "v2 rubric guided",
        "Retrieval": "top_k=5",
        "Quality": 0.86,
        "Latency sec": 2.3,
        "Cost cents": 1.2,
        "Notes": "Best all-around candidate.",
    },
    {
        "Run": "C",
        "Model": "Large model",
        "Prompt": "v3 chain checklist",
        "Retrieval": "top_k=8",
        "Quality": 0.91,
        "Latency sec": 4.8,
        "Cost cents": 4.6,
        "Notes": "Highest quality, expensive and slow.",
    },
]


ARCHITECTURE_LAYERS = [
    {
        "layer": "Enhance Context",
        "examples": "RAG, tool results, memory, user history",
        "watch": "Retrieval hit rate, context length, missing citations, stale sources",
    },
    {
        "layer": "Add Guardrails",
        "examples": "Input validation, output filtering, safety checks, PII redaction",
        "watch": "Blocked requests, unsafe output attempts, redaction misses",
    },
    {
        "layer": "Route and Gateway",
        "examples": "Model routing, rate limiting, auth, logging",
        "watch": "Route decisions, auth failures, model fallback rate, quota pressure",
    },
    {
        "layer": "Reduce Latency",
        "examples": "Semantic caching, prefix caching, streaming",
        "watch": "Cache hit rate, time to first token, p95 response time",
    },
    {
        "layer": "Agent Patterns",
        "examples": "Tool use, multi-step plans, delegation, persistent memory",
        "watch": "Tool errors, loop count, task completion rate, handoff failures",
    },
]


MONITORING_ITEMS = [
    "p50, p95, and p99 latency",
    "Error rate, failed calls, and timeouts",
    "Tokens in, tokens out, and model spend",
    "Requests per second and queue depth",
]


OBSERVABILITY_ITEMS = [
    "Distributed traces across retrieval, model, tools, and post-processing",
    "Structured logs with queryable events",
    "Output quality drift signals",
    "User feedback such as thumbs down, retries, and abandonment",
]


TRIAGE_SCENARIOS = {
    "Responses are suddenly slower": [
        "Check p95 and p99 latency by endpoint.",
        "Inspect traces to see which component slowed down.",
        "Compare cache hit rate and model route decisions against previous runs.",
    ],
    "Answers are less relevant": [
        "Review retrieval scores and retrieved chunks.",
        "Compare output quality drift metrics.",
        "Sample user feedback and retry sessions for patterns.",
    ],
    "Costs increased overnight": [
        "Break down tokens by model and endpoint.",
        "Look for route changes, longer prompts, or lower cache hit rate.",
        "Compare cost per session against the last known-good deployment.",
    ],
}
