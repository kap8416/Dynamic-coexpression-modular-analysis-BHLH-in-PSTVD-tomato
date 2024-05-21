# Dynamic-coexpression-modular-analysis-BHLH-in-PSTVD-tomato

This repository contains the code and resources for a comprehensive study on the effects of mild (M) and severe (S23) strains of Potato Spindle Tuber Viroid (PSTVd) on tomato plants, focusing on symptom development and susceptibility. Our approach integrates transcriptomic and functional genomics data through co-expression and module network analysis.

Key Features:

Tissue-Specific Module Network Analysis: Emphasis on bHLH transcription factor interactions.
CEMiTool Package Utilization: Inference of gene co-expression modules.
Bipartite Network Construction: Analysis for each tissue type.
Motif Exploration: Identification of essential regulatory motifs.

Repository Contents:

Scripts and Code: For performing tissue-specific module network analysis, gene co-expression module inference, bipartite network construction, and motif exploration.
Figure 1: Visual representation of the analysis workflow.

This project aims to deepen the understanding of bHLH transcription factor roles in tomato-PSTVd interactions and provides valuable insights into the regulatory dynamics underlying plant defense mechanisms.


<img width="717" alt="Screenshot 2024-05-20 at 7 41 03 PM" src="https://github.com/kap8416/Dynamic-coexpression-modular-analysis-BHLH-in-PSTVD-tomato/assets/68921776/8ddcceea-00cd-4090-ab59-90ee25586fa0">

Pipeline for the network approaches. (a) Commencing the process, we acquired publicly available microarray expression data encompassing both control and infected leaves and roots.(b) With the obtained expression data, we constructed an expression matrix of each tissue (roots, and leaf separately) and curated additional pertinent files, collectively serving as the foundational input for our subsequent analysis: functional annotation, expression matrix, interest genes interactions, and sample phenotypes (the required  input files are depicted in pink).  (c) We performed a co-expression modular network analysis. This pivotal step was facilitated by the utilization of the CEMiTool, a specialized tool for inferring co-expression modules. (d) Following the completion of the network analysis, we delved into Gene Set Enrichment Analysis (GSEA) performed to unveil significant associations, and functional enrichment analysis was executed on the modules. Furthermore, we identified hub genes residing within the network clusters. (e) Additionally, we constructed bipartite networks delineating the bHLH-regulon interactions. (g) Using our comprehensive network structures, we conducted a final phase of exploration and identified the most representative motifs within each network module.
