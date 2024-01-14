# Cellular Automata Simulator

## Overview
This project implements a simulator for one-dimensional cellular automata. Cellular automata are discrete models studied in computer science, mathematics, and physics to explore complex system behaviors through simple rules.

The simulator allows users to specify the size of the automaton, a rule number that dictates how the automaton evolves over time. The evolution process is visualized through a series of plots, illustrating the changes in the automaton's state over multiple time steps.

## Features
Set Initial State: Create a one-dimensional automaton with a specified size, initializing it with a single active cell in the middle.

Define Rules: Set the behavior of the automaton using an 8-bit binary rule number, influencing the state transitions based on the cell's neighbors.

Evolution: Simulate the evolution of the automaton over a specified number of time steps.

Visualization: Visualize the evolution of the automaton through a plotted image, showing the changing state of the cells.

## Usage
1. Clone the repository to your local machine
```git clone https://github.com/your-username/cellular-automaton-simulator.git```

2. Install poetry
```Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -```

3. Add path to the windows environmental variables:
```%APPDATA%\Python\Scripts```

4. Go to cellularautomata directory.
  ```cd cellularautomata```

### Run the simulation with default parameters (board_size == 1501, rule == 45, steps == 1000)
```poetry run python main.py```

### Run the simulation with specific parameters
```poetry run python main.py --board_size {size} --rule {rule} --steps {steps}```


### View the evolution plot:

The generated evolution plot will be displayed, providing insights into the cellular automaton's dynamic behavior.
![image](https://github.com/weibik/CellularAutomata/assets/57102801/0d3ff436-7010-46cc-ba6a-5ec7c9ec6b52)
