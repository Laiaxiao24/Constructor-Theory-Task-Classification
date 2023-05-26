# Task classification I - Constructor Theory

A program that classifies tasks as possible/impossible based on [Constructor Theory](https://www.constructortheory.org/).

## Table of Contents
* [About the project](##About-the-project)
* [Installation](##Installation)
* [Usage](##Usage)
    * [Tasks generation](###Tasks-generation)
    * [Tasks classification](###Tasks-classification)
* [Project status](##Project-status)
* [Other information](##Other-information) 
* [Contact](##Contact)

## About the project
[Constructor Theory](https://www.constructortheory.org/) is a theory based on the study of transformations which can be possible or impossible.  The central element in this theory are tasks and the way they can be categorized as possible or impossible. 

Therefore, the **aim** of this program is to generate tasks and classify them by following the rules of CT framework. Note that in this program, the rules employed are for the case of reversible tasks.

The program is structured in two parts:
* **Task generation:** tasks are generated from the attributes of the chosen dimension.
* **Task classification** tasks are classified into two methods- Deterministic rules, Guessing Rules.

Once the classification is done, a `.txt` file results as the output with all the possible ways to classify the tasks of the system.

The project is created with `Python 3.9.5`.

## Installation
To run this project, download the folder containing all the code. No further content needs to be installed. Refer to the following section to learn the usage.

## Usage
As mentioned before, the code is divided into two steps: task generation and task classification. In this section, each part is thoroughly explained.

### Tasks generation
The file `task generation.py` generates all the existing tasks given a dimension. The folder includes tasks for the systems of dimension 4. 

When running the file `task generation.py`, the system dimension is required from the user to input. Then the program informs of the number of reversible tasks generated and the attributes used:

![Ex1](https://drive.google.com/uc?export=view&id=12Kl5kslcCBr2hmiJ40ENOYYVwjiLUpDz)

In this version, tasks are represented as lists, in the following format: _[[in,out], [in,out]...]_

All these files are stored in the folder: _Constructor theory/Tasks classification/ Tasks generation_

The tasks are stored both in `.txt` file, which is easy to read for the user, and `.json` file, which is the one used in the program.

Example of tasks (dimension 4):

![Ex2](https://drive.google.com/uc?export=view&id=17SNk9YIeV9GI6XqrwqDHMaZgoRiCBFDK)

### Task classification
The file `task classification.py` carries out the classification of the tasks. Each rule employed is defined as a function, for comprehension purposes.

The data structure in this code is composed of the following elements:
* **Trio**: list containing all the tasks of the given dimension divided in possibles, impossibles, non-classified (also known as purgatory). _([[possibles], [impossibles], [purgatory]])_
* **Decisions**: list containing different trios. ( _[trio1, trio2... trio n]_)

The logic behind the classification is: 
1. **Deterministic rules**: possibility and impossibility rules, which working on a trio, following logical rules, classify some tasks.
2. **Guessing rules**: once the deterministic rules cannot give any further information, a probabilistic game starts, where the guessing rules generate different possible trios that are added to the decisions set. 

These two procedures are done inside a loop which stops once each trio's purgatory is empty (all tasks classified). The deterministic one is carried out first until no more changes are done, and then it follows the guessing part. And why do we keep each "decision" during the guessing part? Well, by probability, we know that at least one of the trios generated will be correct, the others will evolve (by other rules) until a contradiction appears and it is discarded.

To start the project, the user has to specify the set of tasks to begin with, this includes a set of possible tasks, impossible tasks and the rest of them, as we call them, the _purgatory_. The code includes an example that can be run:

![Ex3](https://drive.google.com/uc?export=view&id=1f-HSFD1OTpRkWwcFAp8CoWJ2om2TCuEx)

The tasks the user wants to specify as possible/impossible can be manually indicated (as the example) or by opening the files of the already generated tasks and updating the lists as wished. 

![Ex4](https://drive.google.com/uc?export=view&id=1IKMlXAyyn9Et8EpCjKFTDJVNNaCygaf2)

where _a_ and _b_ represent tasks the user wants to specify. These can be obtained from the already existing tasks, or entered manually using the function `ut_possibles`.

Once the classification is done, the program will generate a `.txt` file containing all the trios generated with the possible/impossible tasks of each.

![Ex5](https://drive.google.com/uc?export=view&id=1C3JLeajNnK93I7tq89C2jmk9mwDFMHw2)

#### Cleaning, contradictions and general control tools
In order to make the task classification easier and more efficient or prevent errors from appearing, there are several procedures carried out:
* **Duplicated tasks deletion**: after each rule is applied to the list of tasks, duplicated tasks are deleted.
* **Possible-Impossible contradiction**: there are several controls that will make the existing trio from decisions be erased if there are tasks both in the possible and impossible list.
* **Maximum number of possible tasks**: if after deleting the duplicated tasks, this list contains the maximum number of tasks possible, it will stop analyzing this set.
* **Duplicated trios**: deletes duplicated trios.
* **Empty purgatories**: if a purgatory is empty, it will stop the classification of that trio's tasks.

The reader must take into consideration that some of these tools are defined in the code, but never used. Despite this, all of them are documented for the user to be implemented if wished.

## Project status
Although this program is oriented to a general system of dimension n, it has only been tested for tasks of dimension 4. In addition, due to the lack of time, the authors consider there's room for improvement. Therefore, here there are some ideas for the reader to be improved.
### Points to be improved
* **Task generation** tasks are constructed mainly using combinatory, which for large sets of data (big dimensions) are a limitation.
* **Data storage** all the data is stored in `.json` files, however, a more sophisticated data set would improve the efficiency.

## Other information
## Contact
For further information, comments or others, don't hesitate to contact us:
* Email: [laiaxiao24@gmail.com](mailto:laiaxiao24@gmail.com)
* Email: [nisetucadaques@hotmail.com](mailto:nisetucadaques@hotmail.com)

## License
MIT License

Copyright (c) [2022] [Laia Xiao Planas Toro]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
