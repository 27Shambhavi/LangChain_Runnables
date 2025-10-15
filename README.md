# LangChain_Runnables

# LangChain Runnable Examples & Custom Chain Implementation

This repository illustrates how to build modular and composable applications with Language Models (LLMs), focusing on the **Runnable** interface that powers modern LangChain application development (LangChain Expression Language or LCEL).

The examples progress from simple, standalone components to a fully custom implementation of a composable chain pipeline.

---

## 📄 File Structure and Concepts Overview

| Filename | Core Concept(s) Demonstrated | Description |
| :--- | :--- | :--- |
| `simple_llm_app.py` | **Basic LLM Invocation & PromptTemplate** | Shows the foundational use of a LangChain `ChatOpenAI` LLM and a `PromptTemplate` to take user input and generate a simple response. |
| `llmchain.py` | **LLMChain (Legacy LangChain Pattern)** | Demonstrates the `LLMChain` class, which combines an LLM and a PromptTemplate into a single, cohesive unit. This was the standard way to create simple chains previously. |
| `pdf_reader.py` | **Retrieval Augmented Generation (RAG)** | A complete example of a RAG pipeline: **Load** a document, **Split** it into chunks, **Embed** them, store them in a **Vector Store** (`FAISS`), and use a **Retriever** to provide context to the LLM for a final, grounded answer. |
| `runnable_demo.py` | **Mock Components & Basic Chain Logic** | Contains custom, pseudo-classes (`NakliLLM`, `NakliLLMChain`) to illustrate the *internal* mechanics of how an LLM and PromptTemplate are combined into a chain, without using the LangChain library's built-in chain class. |
| `Runnable_standarlize.py` | **The Runnable Interface & Pipelining (LCEL Style)** | **The core demonstration.** This file defines a custom **`Runnable`** abstract class and implements it for mock components. The **`RunnableConnector`** class shows how runnables are linked sequentially, passing data from one component to the next, demonstrating the power of composition. |

---

## 💡 Key Takeaway: The Runnable Standard

The file `Runnable_standarlize.py` is the central demonstration of the **Runnable** architecture:

* **Standardized Interface:** All components (prompts, LLMs, parsers) inherit from the `Runnable` class and implement the universal **`invoke()`** method. This allows any component to be swapped in or out easily.
* **Pipelining:** The **`RunnableConnector`** class acts as a sequence builder, taking a list of runnables and executing them in order. This allows complex workflows to be built simply by defining a list of steps:
    $$\text{Prompt} \rightarrow \text{LLM} \rightarrow \text{Output Parser}$$
* **Composition:** The structure allows smaller chains to be combined into larger, more complex workflows, such as chaining a "joke generation" runnable with a "joke explanation" runnable.
