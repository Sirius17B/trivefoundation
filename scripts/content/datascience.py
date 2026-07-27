# Data Science & Analytics — 25 questions, applied-reasoning style.
QUESTIONS = [
{
 "q": "A streaming service shows half its users a red 'Play' button and the other half a green one, randomly assigned, then compares which group clicks play more often over two weeks. What is this experimental method called?",
 "options": [
   "A/B testing — a controlled experiment comparing two variants with users randomly assigned to each, measuring which version produces better outcomes based on real behavioural data rather than opinion",
   "Exploratory data analysis — the initial investigation of an existing dataset to discover patterns, spot anomalies, and form hypotheses, rather than a controlled experiment actively comparing two live variants",
   "K-means clustering — an unsupervised algorithm that groups similar data points together, a technique for finding structure in existing data rather than a controlled experiment comparing two randomly assigned variants",
   "Feature engineering — using domain knowledge to select and transform input variables for a machine learning model, a data-preparation technique unrelated to running a controlled experiment comparing two button colours"
 ],
 "answer": 0,
 "explanation": "A/B testing randomly assigns users to different variants and measures the resulting difference in real behaviour, scaling the scientific method to product decisions — letting a team base a choice like button colour on actual evidence rather than assumption or opinion."
},
{
 "q": "Two data scientists build models to predict loan defaults using the exact same algorithm. One spends most of her time creating a 'debt-to-income ratio' feature from raw salary and debt figures; the other uses only the raw, unprocessed figures directly. Her model performs notably better. What does this illustrate?",
 "options": [
   "Feature engineering — thoughtfully transforming raw data into more informative input variables using domain knowledge often matters more for model performance than the choice of algorithm alone",
   "A/B testing — a controlled experiment comparing two variants with users randomly assigned to each, a technique for comparing live product variants rather than for describing how input data was prepared before modelling",
   "Dimensionality reduction — techniques for reducing the number of features in a dataset while preserving key information, the opposite of what happened here, since a new feature was added rather than removed",
   "Data governance — the framework of policies and processes for managing data as a business asset, an organisational practice unrelated to why one specific model outperformed another on this predictive task"
 ],
 "answer": 0,
 "explanation": "Feature engineering — using domain knowledge to construct more informative variables like debt-to-income ratio from raw figures — often has a bigger impact on model performance than swapping between similar algorithms, since a well-constructed feature can make a pattern the model needs to learn far more directly visible."
},
{
 "q": "A retailer's dashboard shows 'sales dropped 12% last month' (a fact about what already happened), a separate model estimates 'sales will likely drop another 8% next month if nothing changes' (a forecast), and a third system recommends 'offer a 15% discount on slow-moving stock to offset the predicted drop' (a suggested action). What three-part framework does this illustrate?",
 "options": [
   "Descriptive, predictive, and prescriptive analytics — describing what happened, predicting what's likely to happen, and prescribing what specific action to take, representing increasing levels of business value and complexity",
   "A/B testing at three different stages — running three completely separate randomised controlled experiments simultaneously, one for each part of the retailer's overall combined sales dashboard system",
   "Feature engineering at three different stages — transforming three completely separate sets of raw input variables, one specifically for each of the three separate systems described in this particular scenario",
   "Data governance at three different stages — applying three completely separate sets of formal data policies, one specifically for each of the three separate systems described in this particular retail scenario"
 ],
 "answer": 0,
 "explanation": "This is the classic descriptive/predictive/prescriptive progression: descriptive analytics reports what already happened, predictive analytics forecasts what's likely to happen next, and prescriptive analytics goes further, recommending a specific action — each level generally requiring more sophistication and typically delivering more direct business value."
},
{
 "q": "An analyst studying Lagos electricity demand notices consumption reliably spikes every weekday evening and dips every Sunday morning, in a pattern that repeats week after week, and uses this repeating pattern to help plan generation capacity. What kind of analysis is this?",
 "options": [
   "Time series analysis — statistical and machine learning techniques for data collected over time, specifically identifying trends, patterns, seasonality, and anomalies to inform decisions like capacity planning",
   "K-means clustering — an unsupervised algorithm that groups similar data points together into clusters, a technique for finding groupings within data rather than analysing how one variable changes and repeats over time",
   "A/B testing — a controlled experiment comparing two variants with users randomly assigned to each, a technique for comparing live alternatives rather than for identifying repeating patterns in historical time-ordered data",
   "Dimensionality reduction — techniques for reducing the number of features in a dataset while preserving key information, unrelated to identifying a repeating weekly pattern in electricity demand over time"
 ],
 "answer": 0,
 "explanation": "Time series analysis specifically identifies patterns like the repeating weekday-evening spike and Sunday-morning dip described here — trends, seasonality, and anomalies over time — which is exactly the kind of analysis that underlies real electricity demand forecasting and generation capacity planning."
},
{
 "q": "A dataset of patient gene expression contains 10,000 raw measured features per patient, far more than the number of patients available, making the model prone to overfitting and hard to visualise or interpret. A data scientist reduces this to 100 carefully constructed combined features that still capture most of the meaningful variation. What is this technique called?",
 "options": [
   "Dimensionality reduction — techniques that reduce the number of features in a dataset while preserving key underlying information, addressing the 'curse of dimensionality' where too many features relative to samples makes learning harder",
   "Feature engineering in the general sense of adding new individual features one at a time by hand, which is the opposite of what happened here, since the total number of features was substantially reduced, not increased",
   "A/B testing — a controlled experiment comparing two variants with users randomly assigned to each, a technique for comparing live product alternatives rather than for reducing the number of features in an existing dataset",
   "Time series analysis — statistical techniques specifically for data collected over time, a category of technique unrelated to reducing the total number of gene expression features used to describe each individual patient"
 ],
 "answer": 0,
 "explanation": "Dimensionality reduction (techniques like PCA) addresses exactly this scenario: when the number of features vastly exceeds the number of samples, models struggle to learn effectively — reducing to a smaller number of carefully constructed components that still capture most of the meaningful variation makes learning and interpretation far more tractable."
},
{
 "q": "A multinational company discovers that its Lagos office defines 'active customer' differently from its Nairobi office when both teams report on the exact same underlying customer base, causing leadership to receive two different, inconsistent revenue figures for what should be the same metric. What organisational discipline is missing here?",
 "options": [
   "Data governance — the framework of policies, roles, and processes ensuring data is managed consistently as a business asset, including agreed-upon definitions for shared metrics across different parts of an organisation",
   "Feature engineering — using domain knowledge to construct informative input variables for a machine learning model, a technical data-preparation practice unrelated to two offices using inconsistent metric definitions",
   "K-means clustering — an unsupervised algorithm that groups similar data points together, a specific analytical technique unrelated to two offices reporting inconsistent figures due to differing metric definitions",
   "A/B testing — a controlled experiment comparing two variants with users randomly assigned to each, an experimental methodology unrelated to two offices reporting inconsistent figures for the exact same underlying metric"
 ],
 "answer": 0,
 "explanation": "Data governance specifically addresses this kind of inconsistency — establishing agreed-upon definitions, quality standards, and ownership for shared metrics and data across an organisation, so that 'active customer' means the same thing everywhere it's reported, preventing exactly the kind of conflicting-numbers confusion described here."
},
{
 "q": "Before building any predictive model, a data scientist first spends a day just plotting distributions, checking for missing values, and looking for obvious outliers in a new dataset, discovering that 5% of recorded prices are negative — clearly a data entry error. What practice does this illustrate, and why is skipping it risky?",
 "options": [
   "Exploratory data analysis (EDA) — investigating a dataset before modelling to catch issues like errors, missing values, or unrealistic outliers; skipping it risks building a model confidently on top of flawed, uncorrected data",
   "A/B testing — running a controlled experiment comparing two live variants with users randomly assigned to each, a technique for comparing product alternatives rather than for investigating a dataset before modelling begins",
   "Dimensionality reduction — reducing the number of features in a dataset while preserving key information, a technique for simplifying an already-clean dataset rather than for initially discovering and catching data quality issues",
   "Data governance — the organisational framework of policies and processes for managing data consistently across a company, a broader organisational practice distinct from a single analyst's initial hands-on dataset investigation"
 ],
 "answer": 0,
 "explanation": "Exploratory data analysis surfaces exactly this kind of issue — negative prices that are clearly a data entry error — before any modelling begins. Skipping it risks training a model confidently on top of flawed data, producing results that look plausible but are quietly undermined by uncorrected errors baked into the training set."
},
{
 "q": "A data science competition is consistently won by models using gradient boosting (like XGBoost) on structured, tabular data (spreadsheet-like rows and columns), often outperforming deep learning approaches on this specific kind of data without needing massive computing resources. What does gradient boosting do differently from training one single model?",
 "options": [
   "It builds an ensemble of trees sequentially, with each new tree specifically focused on correcting the errors the current combined ensemble still gets wrong, gradually improving overall accuracy through this iterative correction process",
   "It builds a single, very large decision tree with as many branches as possible, then simply stops improving once that one tree reaches its maximum possible depth, with no further sequential ensemble-building process involved",
   "It works by randomly guessing the correct output for each row and gradually refining those guesses purely through repeated random chance, without ever actually examining the errors made by any previous model",
   "It requires converting the entire tabular, structured dataset into an unstructured, non-tabular text-based format first, since it fundamentally cannot process structured, row-and-column data in its normal original form"
 ],
 "answer": 0,
 "explanation": "Gradient boosting builds trees sequentially, with each new tree specifically targeting the residual errors of the current combined ensemble — iteratively focusing effort where the model is still weak. This targeted, iterative correction is a big part of why it performs so well on structured tabular data, often beating more computationally expensive approaches."
},
{
 "q": "A model trained on medical data is either too simple (missing real patterns in the data, performing poorly on both training and new data) or too complex (fitting noise in the training data too closely, performing great on training data but poorly on new data). What is this fundamental tension between the two failure modes called?",
 "options": [
   "The bias-variance tradeoff — the tension between underfitting (high bias, too simple to capture real patterns) and overfitting (high variance, too sensitive to noise), with a well-tuned model balancing appropriately between the two",
   "The CAP theorem — a principle describing an unavoidable tradeoff in distributed database systems between Consistency, Availability, and Partition tolerance, a concept from distributed systems rather than from model complexity",
   "Feature engineering — using domain knowledge to construct more informative input variables for a model, a data-preparation practice distinct from the underlying tension between a model being too simple versus too complex",
   "A/B testing — a controlled experiment comparing two variants with users randomly assigned to each, an experimental methodology distinct from the underlying tension between a model's simplicity and its complexity"
 ],
 "answer": 0,
 "explanation": "The bias-variance tradeoff names exactly this tension: high bias means a model is too simple and misses real patterns (underfitting), while high variance means it's too sensitive to the specific noise in its training data (overfitting) — good models are tuned to sit at a reasonable balance point between these two failure modes."
},
{
 "q": "A fintech company applies an unsupervised algorithm to millions of transaction records with no pre-labelled categories, and it automatically groups customers into distinct clusters — one of low-income frequent small transactions, another of salaried monthly bill payments, and a third of business-owner high-frequency mixed transactions — without ever being told these categories in advance. What technique produced this result?",
 "options": [
   "K-means clustering — an unsupervised algorithm that partitions data into groups by iteratively assigning each point to its nearest centroid, discovering natural groupings in data with no pre-existing labels needed",
   "A/B testing — a controlled experiment comparing two variants with users randomly assigned to each, a technique requiring an active, deliberate comparison rather than discovering natural groupings within existing unlabelled data",
   "Gradient boosting — a supervised ensemble method that requires labelled training examples with known correct answers, the opposite of what's described here, since no pre-existing category labels were provided at all",
   "Time series analysis — statistical techniques specifically for data collected over time, a category of technique unrelated to discovering natural groupings among customers based on their overall transaction patterns"
 ],
 "answer": 0,
 "explanation": "K-means clustering is a classic unsupervised technique that discovers natural groupings in data with no pre-existing labels, partitioning points into clusters based on similarity — exactly the kind of customer segmentation described here, genuinely useful for tailoring financial products to each discovered segment's actual needs."
},
{
 "q": "A news article claims 'ice cream sales and drowning deaths are strongly correlated, so ice cream must cause drowning.' What is the most likely actual explanation, and what statistical principle does this illustrate?",
 "options": [
   "Correlation doesn't imply causation — both ice cream sales and drowning deaths independently rise in hot summer weather, a confounding variable, without either one actually causing the other directly",
   "The bias-variance tradeoff — a concept specifically about a machine learning model being too simple or too complex, unrelated to whether a correlation observed between two real-world variables implies one directly causes the other",
   "Feature engineering — using domain knowledge to construct informative input variables for a model, a data-preparation concept unrelated to whether an observed correlation between two variables implies genuine causation",
   "Dimensionality reduction — techniques for reducing the number of features in a dataset, a concept unrelated to whether a statistical correlation observed between two specific real-world variables implies genuine causation"
 ],
 "answer": 0,
 "explanation": "This is a classic illustration of 'correlation doesn't imply causation': hot weather is a confounding variable driving both more ice cream sales and more swimming (and therefore more drowning) independently — the two statistics move together without either one causing the other, a foundational caution in interpreting any observed statistical relationship."
},
{
 "q": "A rare-disease detection model trained on a dataset where 99% of examples are healthy and only 1% have the disease can achieve 99% accuracy simply by always predicting 'healthy', while being completely useless at its actual job of detecting the disease. What problem does this illustrate, and why is raw accuracy a misleading metric here?",
 "options": [
   "Class imbalance — when one outcome vastly outnumbers another in the training data, raw accuracy becomes misleading since a model can score very high while being useless at correctly identifying the rare, actually important class",
   "The bias-variance tradeoff — a concept specifically about a model being too simple versus too complex, a distinct issue from the specific problem of one class vastly outnumbering another within a dataset's actual composition",
   "Dimensionality reduction — techniques for reducing the number of features in a dataset while preserving key information, a data-preparation concept unrelated to one outcome class vastly outnumbering another within the same dataset",
   "A/B testing — a controlled experiment comparing two variants with users randomly assigned to each, an experimental methodology unrelated to how a dataset's actual outcome classes happen to be numerically distributed"
 ],
 "answer": 0,
 "explanation": "Class imbalance makes raw accuracy a genuinely misleading metric: with 99% healthy examples, a model that always predicts 'healthy' scores 99% accuracy while being clinically useless — which is why metrics like precision, recall, or F1-score (that specifically account for how well the rare, important class is actually detected) are used instead in imbalanced scenarios like this."
},
{
 "q": "A machine learning model scores 95% accuracy when tested on the same data it was trained on, but a more honest evaluation splits the data into multiple folds, training on some and testing on the held-out remainder, repeating this process several times and averaging the results. What is this more rigorous evaluation technique called?",
 "options": [
   "Cross-validation — repeatedly splitting data into training and held-out testing portions and averaging performance across the splits, giving a more honest, reliable estimate of how a model will perform on genuinely new data",
   "K-means clustering — an unsupervised algorithm that groups similar data points together into clusters, a technique for discovering structure in unlabelled data rather than for rigorously evaluating a trained model's true performance",
   "Feature engineering — using domain knowledge to construct informative input variables for a model, a data-preparation technique applied before training rather than a technique used specifically to evaluate a model afterward",
   "Data governance — the organisational framework of policies and processes for managing data consistently, a broader organisational practice distinct from the specific technical process of rigorously evaluating one trained model"
 ],
 "answer": 0,
 "explanation": "Cross-validation repeatedly splits data into training and held-out testing portions, averaging results across the splits, which gives a far more honest estimate of real-world performance than testing on the exact same data used for training — a technique specifically designed to catch the kind of inflated, overly optimistic accuracy that testing on training data alone can produce."
},
{
 "q": "An online retailer trains a demand-forecasting model using only the last three months of sales data, missing an entire holiday shopping season, and the model consequently underpredicts demand badly every December. What data-related issue does this illustrate?",
 "options": [
   "Sampling bias (specifically, unrepresentative training data) — training data that doesn't cover the full range of relevant real-world conditions (like a full annual cycle including holiday seasonality) produces a model that fails outside that narrow window",
   "The CAP theorem — a principle describing an unavoidable tradeoff in distributed database systems during a network partition, a concept from distributed systems engineering unrelated to a forecasting model's underlying training data coverage",
   "A merge conflict — a situation where version control can't automatically reconcile two developers' changes to the same file, a source-control concept entirely unrelated to a forecasting model's underlying training data coverage",
   "Containerisation — a technology for packaging an application with its exact runtime dependencies into a portable unit, a deployment concept entirely unrelated to whether a forecasting model's training data actually covers a full year"
 ],
 "answer": 0,
 "explanation": "Training on only three months of data that happens to miss the holiday season means the model never saw that seasonal pattern at all, so it has no learned basis for predicting it — a sampling bias problem where the training data simply doesn't represent the full range of conditions the model will actually be used to predict."
},
{
 "q": "A weather app claims '90% chance of rain tomorrow' based on a model trained on historical weather patterns. A user asks how confident they should be in this specific number. What is the most accurate way to think about this kind of probabilistic forecast?",
 "options": [
   "It reflects the model's estimated likelihood based on patterns in historical data, not a certainty — real-world outcomes are inherently uncertain, and a well-calibrated model's 90% predictions should actually be right about 90% of the time across many such predictions",
   "It should be treated as an absolute, guaranteed certainty, since any professionally built weather forecasting model would never publish a specific percentage figure unless it was completely and mathematically certain of the outcome",
   "The specific number is essentially meaningless and arbitrary, since weather forecasting models are, as a general rule, no more accurate than randomly guessing whether it will rain on any given day",
   "It reflects the forecaster's personal individual opinion about tomorrow's weather rather than reflecting any actual underlying statistical pattern derived from real historical weather data of any kind"
 ],
 "answer": 0,
 "explanation": "A well-calibrated probabilistic forecast means that across many predictions made with '90% chance', roughly 90% of those days should actually see the predicted outcome — it's a genuine, data-derived estimate of likelihood, not a certainty and not an arbitrary guess, and understanding this distinction matters for correctly interpreting any probabilistic model's output."
},
{
 "q": "A dataset of customer ages includes a few entries of '150' and '-5', which are obviously impossible ages caused by data entry mistakes, sitting far outside the range of every other reasonable value. If left unaddressed before training a model, what risk do these values pose?",
 "options": [
   "Outliers like these can disproportionately skew statistical summaries (like the average) and distort what a model learns, since a model may end up allocating undue importance to these clearly erroneous, extreme values",
   "Outliers of this kind have no real practical effect on any statistical summary or any machine learning model whatsoever, and can always be safely left completely unaddressed with no consequence to the analysis",
   "The presence of any outlier values in a dataset always guarantees that a trained machine learning model will achieve exactly 100% accuracy on all future new data, regardless of how those specific extreme values are actually handled",
   "Outlier values like '150' and '-5' can only ever occur in an age column specifically, and this exact category of data quality issue is structurally and definitionally impossible to occur in any other type of numeric column"
 ],
 "answer": 0,
 "explanation": "Outliers, especially clearly impossible ones caused by data entry errors, can disproportionately distort statistical summaries like averages and can skew what a model learns during training, which is exactly why outlier detection and handling is a standard, important part of data cleaning before serious analysis or modelling begins."
},
{
 "q": "A political poll surveys 1,000 people by calling landline phones during weekday business hours, systematically missing younger people who mostly use mobile phones and are usually at work or school during that time. The poll's results end up skewed toward older, retired respondents. What problem does this illustrate?",
 "options": [
   "Sampling bias — the method used to select survey respondents systematically excludes or under-represents certain groups, producing results that don't accurately reflect the actual broader population being studied",
   "The bias-variance tradeoff — a concept specifically about a machine learning model being too simple or too complex, a distinct technical issue from a survey's data-collection method systematically excluding certain demographic groups",
   "Cross-validation — a technique for evaluating a trained model's performance by repeatedly splitting data into training and testing portions, a concept unrelated to whether a poll's original data-collection method itself is representative",
   "Class imbalance — a situation where one outcome vastly outnumbers another within an existing dataset's labels, a distinct issue from a survey's data-collection method itself systematically excluding certain demographic groups"
 ],
 "answer": 0,
 "explanation": "This is a textbook sampling bias: the specific method used to reach respondents (landlines, weekday business hours) systematically excludes younger, more mobile-reliant, employed people, meaning the resulting sample simply doesn't represent the actual broader population, regardless of how carefully the 1,000 responses that were actually collected are later analysed."
},
{
 "q": "An analyst studying successful Nigerian tech startups only interviews founders of companies that are still operating today, concluding 'all successful startups pivoted their business model at least once.' What flaw does this analysis contain?",
 "options": [
   "Survivorship bias — only studying the surviving, successful cases while ignoring the (likely much larger) set of startups that also pivoted but still failed, which would undermine the conclusion that pivoting itself was the deciding factor",
   "Dimensionality reduction — reducing the number of features in a dataset while preserving key information, a data-preparation technique unrelated to whether an analysis draws its sample only from surviving, successful companies",
   "Feature engineering — using domain knowledge to construct informative input variables for a model, a modelling-preparation technique unrelated to whether an analysis draws its underlying sample only from surviving companies",
   "The CAP theorem — a principle describing an unavoidable tradeoff in distributed database systems, a concept from distributed systems engineering entirely unrelated to whether a business analysis draws its sample only from survivors"
 ],
 "answer": 0,
 "explanation": "Survivorship bias means studying only the cases that 'survived' (successful, still-operating startups) while ignoring the failures — many of which likely also pivoted but still failed. Without comparing to the failures, there's no way to tell whether pivoting actually caused success or was simply a common, unremarkable action many startups take regardless of eventual outcome."
},
{
 "q": "A chart showing company revenue over five years uses a Y-axis that starts at ₦9.8 million instead of ₦0, making a modest 5% revenue increase visually look like the bar roughly doubled in height. What data visualisation problem does this illustrate?",
 "options": [
   "A misleading or truncated axis — manipulating a chart's scale (like a non-zero baseline) can visually exaggerate a small real difference, distorting how a viewer perceives the actual underlying data even though the numbers themselves are technically accurate",
   "Class imbalance — a situation where one outcome vastly outnumbers another within a dataset's labels, a concept about the composition of training data for a model rather than about how a chart's visual axis and scale are constructed",
   "The bias-variance tradeoff — a concept specifically about a machine learning model being too simple or too complex, a distinct technical concept unrelated to how a chart's Y-axis scale is chosen and displayed to a viewer",
   "Dimensionality reduction — techniques for reducing the number of features in a dataset while preserving key information, a data-preparation concept unrelated to how a chart's Y-axis scale is chosen and visually displayed"
 ],
 "answer": 0,
 "explanation": "A truncated or non-zero-baseline axis is a well-known way charts can mislead: the underlying numbers may be entirely accurate, but the visual impression created — a small change looking dramatic — misleads a viewer's intuitive interpretation, which is why honest data visualisation practice generally recommends starting bar charts at zero unless there's a clearly labelled, deliberate reason not to."
},
{
 "q": "An e-commerce analyst wants to know 'did our new homepage design cause more purchases, or did purchases just happen to rise anyway due to the approaching holiday season?' What is the most reliable way to isolate the actual causal effect of the homepage design itself?",
 "options": [
   "A randomised controlled experiment (like an A/B test) — randomly assigning users to see the old or new homepage during the same time period isolates the design's specific effect from other factors like seasonality that would affect both groups equally",
   "Simply comparing this year's holiday-season purchase numbers to last year's pre-redesign holiday-season numbers, since any difference between two different years must necessarily be caused entirely by the specific homepage redesign alone",
   "Asking a small focus group of five people whether they personally like the new homepage design better, since personal subjective opinions expressed in an interview reliably and directly measure actual real purchasing behaviour",
   "There is no way to ever reliably distinguish the actual causal effect of a homepage design change from other simultaneously occurring external factors like an approaching holiday season, regardless of the analytical method used"
 ],
 "answer": 0,
 "explanation": "A randomised experiment run during the same time period, with users randomly split between old and new designs, is specifically designed to isolate the causal effect of the change itself — since both groups experience the same seasonal effects simultaneously, any real difference in purchase rate between the groups can be attributed to the design change rather than confounded with an approaching holiday season."
},
{
 "q": "An ensemble method trains hundreds of decision trees, each on a random subset of both the data rows and the available features, then combines all their individual predictions by majority vote (for classification) or averaging (for regression). What is this technique called, and why does it typically outperform any single decision tree?",
 "options": [
   "Random forest — combining many trees trained on random subsets of data and features reduces the high variance (overfitting tendency) of any single decision tree, since the ensemble's combined vote is far more stable than one tree alone",
   "K-means clustering — an unsupervised algorithm that groups similar data points together into clusters based on proximity, a fundamentally different technique from an ensemble method that combines many supervised decision trees",
   "A/B testing — a controlled experiment comparing two variants with users randomly assigned to each, an experimental methodology for comparing live alternatives rather than a modelling technique for combining many trained trees",
   "Time series analysis — statistical techniques specifically for data collected over time, a category of technique unrelated to an ensemble method that combines the predictions of many independently trained decision trees"
 ],
 "answer": 0,
 "explanation": "A single decision tree is notoriously sensitive to its exact training data — small changes can produce a very different tree (high variance, prone to overfitting). Random forest trains many trees on random subsets of rows and features and combines their votes, which averages out that instability, typically producing a far more stable and accurate model than any single tree alone."
},
{
 "q": "A hospital's dataset has 15% of blood pressure readings missing entirely, and a data scientist must decide how to handle these gaps before training a model. Simply deleting every row with any missing value would discard 40% of the entire dataset. What is a commonly used alternative approach, and what should be considered when choosing one?",
 "options": [
   "Imputation — filling in missing values using a reasonable estimate (like the average, a more sophisticated model-based prediction, or a value carried from a similar record), while considering whether the missingness itself might be meaningful rather than random",
   "Dimensionality reduction — reducing the total number of measured features in the dataset, a technique addressing having too many columns rather than addressing missing values within the existing rows and columns",
   "K-means clustering — an unsupervised algorithm that groups similar data points together, a technique for discovering structure in complete data rather than specifically for filling in individually missing values within a dataset",
   "The bias-variance tradeoff — a concept specifically about a trained model being too simple or too complex, a distinct issue unrelated to the practical question of how to handle missing values in a dataset before training even begins"
 ],
 "answer": 0,
 "explanation": "Imputation fills in missing values with a reasonable estimate rather than discarding potentially large amounts of otherwise-valid data — but a careful analyst also considers whether values are missing randomly or systematically (for example, sicker patients might be less likely to have every measurement recorded), since that pattern itself can carry meaningful information that naive imputation might otherwise erase."
},
{
 "q": "A study reports 'the new teaching method improved test scores, and the difference was statistically significant (p < 0.05).' A student who has never studied statistics asks what this specific phrase actually tells them. Which explanation is most accurate?",
 "options": [
   "It suggests the observed difference is unlikely to have occurred purely by random chance alone, based on a specific statistical threshold — though statistical significance alone doesn't guarantee the difference is large or practically important",
   "It means the result is 95% certain to be true and completely correct in every respect, with the specific number 0.05 representing a guaranteed, absolute upper bound on how wrong the reported study's conclusion could possibly be",
   "It means the new teaching method is proven, beyond any conceivable doubt, to be the single best possible teaching method that could ever exist for any student in any subject under any circumstances whatsoever",
   "The specific phrase 'statistically significant' is essentially meaningless marketing language commonly used by researchers, and carries no real, substantive mathematical meaning whatsoever within any actual formal study"
 ],
 "answer": 0,
 "explanation": "Statistical significance (commonly using a threshold like p < 0.05) indicates the observed difference is unlikely to be purely random chance, given the specific statistical test used — but it's a narrower claim than many people assume: it says nothing directly about how large or practically meaningful the effect actually is, which is a separate and equally important consideration."
},
{
 "q": "Which of the following are genuine, well-recognised risks of relying purely on 'raw accuracy' to evaluate a fraud-detection model, given that genuine fraud cases are typically a very small fraction of all transactions? Select all that apply.",
 "options": [
   "A model that never flags anything as fraud can still achieve very high raw accuracy, despite being completely useless at its actual job",
   "Raw accuracy doesn't distinguish between a model that's good at catching real fraud and one that's simply good at recognising the much more common non-fraud cases",
   "Raw accuracy is mathematically undefined and cannot be calculated at all whenever a dataset contains any class imbalance of any kind",
   "A model can improve its raw accuracy score by getting slightly better at the common case while getting no better (or even worse) at detecting the rare, actually important fraud cases"
 ],
 "answer": [0, 1, 3],
 "multi": True,
 "explanation": "These are all genuine, well-documented issues with raw accuracy under class imbalance — a model can score deceptively high while being useless at its actual job of catching rare fraud cases. Raw accuracy is not mathematically undefined in imbalanced datasets, though; it's perfectly calculable, it's simply a misleading metric to rely on alone in that situation."
},
{
 "q": "Which of the following are genuine examples of a confounding variable creating a misleading correlation between two unrelated things? Select all that apply.",
 "options": [
   "Ice cream sales and drowning incidents both rising in summer, due to hot weather independently driving both",
   "Countries with more registered doctors per capita also tending to have higher recorded rates of a certain disease, partly because more doctors means more diagnoses are actually made and recorded",
   "A study finding that taller people, on average, know more words than shorter people, largely explainable by age, since older children are both taller and have learned more words than younger children",
   "A company observing that its revenue increased in the same month it changed its office's paint colour, with no other plausible explanation of any kind investigated or considered whatsoever"
 ],
 "answer": [0, 1, 2],
 "multi": True,
 "explanation": "Hot weather, more thorough diagnosis due to more doctors, and age are all genuine, classic examples of a third variable (a confounder) independently driving both halves of an observed correlation. The paint colour example isn't really illustrating a confounding variable — it's simply illustrating jumping to a causal conclusion from a single coincidental data point with no serious investigation of any explanation at all, confounding or otherwise."
},
]
