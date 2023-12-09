# bridge-capacity-analysis

## Overview
The Bridge Capacity Analysis Tool is a Python utility designed for analyzing bridge capacity data. It processes XLSX format reports and generates an Excel report with detailed insights.

## Objectives
### Support for GTM and Sales Teams:
* Facilitates planning for sales pipelines.
* Enhances customer conversations with detailed GPU allocation data.
### Strategic Resource Allocation:
* Aids the Strategy and Ops team in allocating capacities to reserved and on-demand cloud.

## Key Features
Data Processing: Reads a bridge capacity allocation report in XLSX format.
Report Generation: Outputs an Excel file with three informative tabs:
* Tab 1: Regional and Cluster Capacity Overview
** Displays total allocated and available GPUs by region and cluster.
* Tab 2: GPU Availability by Type
** Provides a pivot table of GPUs available, categorized by type.
* Tab 3: VM Shape-GPU Type Mapping
** Shows the mapping between VM shapes and associated GPU types.

## Usage
* Input Requirement: Bridge capacity allocation report in XLSX format.
* Output: An Excel file with three tabs, offering different perspectives on GPU resources.
