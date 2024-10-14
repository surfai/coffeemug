## QueryExtractNode

The `QueryExtractNode` is a crucial component in the taiphi library, designed to extract structured information from unstructured text using large language models (LLMs). This node is particularly useful for converting free-form text into a structured format based on a predefined schema.

### Overview

The `QueryExtractNode` operates by:

1. Taking an input text and a schema as inputs.
2. Utilizing an LLM to analyze the text and extract relevant information.
3. Structuring the extracted information according to the provided schema.
4. Returning the structured data in a format that adheres to the schema.

This node is especially valuable in scenarios where you need to:
- Extract specific data points from lengthy documents or conversations.
- Convert unstructured user inputs into structured data for further processing.
- Automate the parsing of complex text into predefined data structures.

### Key Features

- Flexible schema definition: Allows users to define custom schemas for data extraction.
- LLM-powered extraction: Leverages the power of large language models for intelligent text analysis.
- Structured output: Ensures that the extracted data is returned in a consistent, structured format.
- Customizable prompts: Enables fine-tuning of the extraction process through customizable LLM prompts.

### Usage

The `QueryExtractNode` can be integrated into various data processing pipelines, particularly those dealing with natural language inputs. It serves as a bridge between unstructured text and structured data, making it an essential tool for tasks such as:

- Information retrieval from documents
- Automated form

::: taiphi.queryextract

