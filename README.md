# Cortex Certifai Examples

This directory contains examples and tutorials illustrating how to use Certifai in a notebook environment and CLI.

## Notebooks

The *notebooks* folder contains JupyterLab notebooks which demonstrate how to use various functions of Certifai in a notebook environment. Instructions for getting started with the notebooks and descriptions of the sample notebooks available in this repo and the Certifai Toolkit can be found [here](https://cognitivescale.github.io/cortex-certifai/docs/toolkit/notebook-usage/jupyter).

## Tutorials

The *tutorials* folder contains walkthroughs which demonstrate basic Certifai functionality. A list of tutorials available in this repo can be found in the [tutorials README](/tutorials/README.md).

## Models

The *models* folder contains examples of wrapping trained models into services that can be scanned with Certifai. See the [models README](/models/README.md) for more information.

## Certifai Documentation

Refer to the Cortex Certifai documentation: https://cognitivescale.github.io/cortex-certifai/docs/about for detailed information about Cortex Certifai.

## Notebooks Table of Contents

| Notebook Name | Description | Task Type | Model Types | Evaluation Types | Key Properties |
| --- | --- | --- | --- | --- | --- |
| [AnalyzeFeatureUsage.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/analyze_feature_usage) - Analyzing Feature Usage | Illustrates the use of Certifai to create and run an explanations scan of a locally defined model from first principles. It then analyzes and displays feature distribution of the counterfactuals.  |  Binary classification | Decision Tree <br /> Logistic Regression | Explanations |  Feature importance |
| [BringInYourOwnModel.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/tutorials/bringing_in_your_own_model/part_one) - Building a scan programmatically with your own model | A tutorial that takes data scientists through model preparation and scan. This notebook/tutorial is also packaged as part of the toolkit and can be accessed at `examples/notebooks/BringingInYourOwnModel.ipynb`. | Binary Classification | Logistic Regression | Fairness  <br /> Explainability <br />  Robustness | How to integrate your own model |  
| [CertifaiSageMakerExample.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/sagemaker) - Running Cortex Certifai Scan on Sklearn model built and deployed on AWS Sagemaker using Certifai Model Connectors | Uses Sagemaker notebook instance to create sklearn models to classify german credit loan risk (predict whether loan will be granted or not) and evaluate fairness. | Binary Classification | SVM <br /> Logistic Regression | Fairness | Sagemaker |
| [CleanStart.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/clean_start) - Building a scan programmatically |  Illustrates the use of Certifai to create and run a fairness scan of a locally defined model from first principles. Again, one of the scan runs produced by this notebook will be saved for viewing |  Binary classification |  SVM <br /> Logistic Regression |  Fairness | Integrating a notebook model <br /> Preflight checks |
| [CleanStart(soft-output).ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/clean_start) - Building a scan programmatically |  A version of the CleanStart notebook for models that produce soft outputs (like probabilities) rather than discrete labels. |  Binary classification | SVM <br /> Logistic Regression | Fairness | Soft or probabilistic outputs |
| [CleanStartSegmented.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/segmented_model_demo) - Building a scan programmatically |  Provides an initial illustration of how to accommodate segmented models in Certifai notebooks. |  Binary classification | SVM <br /> Logistic Regression  | Fairness |  Segmented or federated models |
| [FairnessMetrics.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/fairness_metrics) - Using Different Fairness Metrics | Builds a scan definition to perform multiple fairness analyses other than the burden-based default used by the Certifai counterfactual framework. Specifically, it examines two widely used measures of fairness: demographic parity and equal opportunity. | Binary Classification | SVM <br /> Logistic Regression | Fairness | Demographic parity <br /> Equal opportunity <br /> Using ground truth |
| [FastExplanationsAdultIncome.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/fast_explanations) - Fast explanations for bulk explanation production | Illustrates how to explain large number of examples with a fast approximation following a global precalculation step. | Binary Classification | Random Forest |Explanations <br /> Performance | Bulk explanation |
| [german_credit_azure_ml_demo.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/azureml_model_headers_demo) | Takes data scientists through the end-to-end process of building credit risk (loan approval) models, deploying the models as containerized web services with header-based authentication in an Azure-ML workspace, and running a Certifai scan to analyze model fairness. | Binary Classification  | SVM <br /> Logistic Regression | Fairness | Azure Machine Learning Notebook VM  |
| [HiddenFeatures.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/hidden_features) |  Illustrates the use of Certifai to analyze bias towards protected classes in a model. We show there can still be residual unfairness even if the model is not given access to the protected features. |  Binary classification |  Logistic Regression |  Fairness |  hidden features <br /> Fairness through unawareness |
| [interpreting_certifai_fairness_robustness_scores.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/interpreting_scores/notebooks/interpreting_fairness_robustness_scores) - Examination of robustness and fairness on simulated datasets | This notebook uses binary classification models trained on simple simulated datasets to build intuition around the robustness and fairness scores. | Binary classification | Multilayer Perceptron (MLP) | Fairness <br /> Performance-Accuracy  <br /> Robustness | interpreting scores |
| [MulticlassHeartDisease.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/multiclass) | Illustrates the use of Certifai to create and run a scan on local multiclass classification models that predict the presence of heart disease (angiographic disease status). Two scans are run against the models that frame the use case as a partitioned and ordered multiclass classfication tasks respectively. | Multiclass classification | SVM <br /> Logistic Regression  | Robustness <br /> Explainability <br /> Explanation <br /> Fairness <br /> Performance | Ordered Multiclass <br /> Partitioned Multiclass |
| [UnorderedMulticlass.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/multiclass) | Illustrates the use of Certifai to create and run a scan for an unordered multiclass-classification use case where the outcome classes are neither favorable nor unfavorable. | Multiclass classification | SVM <br /> Logistic Regression  | Robustness <br /> Explainability <br /> Performance <br /> | Unordered Multiclass |
| [patient_readmission_xxx.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/patient_readmission) | A healthcare example illustrating counterfactual explanations and trust score scanning, using data that is one-hot encoded. Explanations and scores are viewed in the Console and analyzed in a notebook. | Binary Classification | MLP Classifier <br /> Logistic Regression | Explanation <br /> Fairness | One-hot encoding <br /> Save/load scan definition <by /> Preflight checks  |
| [PracticalIssues.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/practical_issues) | Illustrates a couple of practical issues that may occur in typical deployments: <br /> - Pre-encoded data - this notebook shows how to handle datasets in which categorical features have already been encoded as one-hot columns (e.g. - by an ETL process). Explanations are still surfaced with normal categorical values, and the results will be equivalent to those which would have been obtained using an unencoded dataset (with a suitable encoder for the model). <br /> - Bucketing of granular or continuous fairness grouping features | Binary Classification | SVM <br /> Logistic Regression | Fairness | One-hot encoding <br /> Fairness feature bucketing |
| [Regression.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/regression) | Illustrates the use of Certifai to create and run a scan including Robustness, Explainability, Explanations, Fairness, and Performance on local regression models that predict the settled claim amount on auto insurance claims. This notebooks also includes running a preflight scan on the local models to identify possible issues that may affect the scan and produce time estimates for the scan. | Regression | SVM <br /> Lasso | Robustness <br /> Explainability <br /> Explanations <br /> Fairness <br /> Performance | Regression <br /> Preflight Checks |
| [Regression-Variants.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/regression) | Illustrates alternate formulations for regression problems. | Regression | SVM <br /> Lasso | Explanations | Regression alternate formulations |
| [TargetEncoding.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/practical_issues) | Illustrates further issues that may occur in typical deployments: <br /> - Target-encoded data - this notebook shows how to handle datasets in which categorical features have been target-encoded. Multiple counterfactual explanations are surfaced with mapped categorical values. <br /> - Bucketing of target-encoded fairness grouping features | Binary Classification | SVM <br /> Logistic Regression | Fairness <br /> Explanation | Target-encoding <br /> Fairness feature bucketing <br /> Multiple counterfactuals <br /> Demographic Parity |
| [ScanFromDefinition.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/scan_from_definition) - Running the scanner within a notebook from a definition file  | Illustrates the use of Certifai to generate reports based upon an existing scan definition, with multiple models and multiple analysis types which can be run as a single evaluation.   | Binary classification  | Logistic Regression  |  Fairness | Using the scanner from a notebook |
| [SHAP.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/shap) - SHAP explanations | Illustrates the use of an alternative explanation type (Kernel SHAP) to provide both an explainability measure for a model and explanations for individual predictions. SHAP may be used as an alternative to Certifai counterfactual explanation in circumstances where feature weights rather than counterfactual exemplars are preferred. | Binary Classification | SVM <br /> Logistic Regression | Explanations  | SHAP Explanations |
| [xgboostDmatrixExample.ipynb](https://github.com/CognitiveScale/cortex-certifai-examples/tree/master/notebooks/xgboost-model) - Running Cortex Certifai fairness evaluation on xgboost model to predict adult income | Illustrates how to accommodate Xgboost models trained with DMatrix data structure in Certifai Notebooks. | Binary Classification | Xboost (XBG) | Fairness | Handling models with implicit data encodings |
