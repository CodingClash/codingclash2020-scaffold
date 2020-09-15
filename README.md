# codingclash2020-scaffold

## Engine Installation
To install the engine as a local package, open your [terminal](https://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it) and run

```
pip install --upgrade codingclash2020
```

Then, to install the requirements for the engine, run

```
pip install -r requirements.txt
```

(Depending on how your pip is set up, you may need to replace `pip` with `pip3`.) 

## Sample code
Under the _bots/_ folder, you will notice that there are 2 example bots. In each folder, _bot.py_ contains the AI code that will run on each bot. The first bot, _template/_, is a barebones shell of what you will need. The second bot, _sample/_, has all of the functions that you may use implemented and has a little bit of strategy to get you started. Each of the folders also contains a _stubs.py_, which includes all of the methods that you can call in your bot code. At the top of _bot.py_, there's a line to import _stubs.py_. _stubs.py_ contains headers for each of the methods that you can use so that IDEs don't get mad about the different methods that you call not existing.

## Running

Run a sample game! Use:

```
python3 run.py bots/sample/ bots/sample/ --save replay.txt
```

Here, there are many arguments to _run.py_. The first two arguments are required, and are the paths to the folders containing _bot.py_ for the blue team and the red team respectively.

The next argument shown above *--save*, and the filepath that you provide to that argument is where the replay file of the game will be saved. This replay file can later be loaded into the visualizer for you to view the game.

You should see the turn numbers outputted to your console as each round ends. 
When the game is over, the replay info will be stored in replay.txt 
(you can use other names for the replay file as well). You can upload the replay file
to the visualizer to watch the game play out.

Place the folder with your own bot code and stubs.py inside the *bots/* folder. If your
folder is named *yourcode/*, for example, you can run a game between the sample bot and 
your bot using:

```
python3 run.py bots/sample/ bots/yourcode/ --save replay.txt
```

## More options

Currently, the game ends after 200 rounds. However, if you want the games to continue
until 500 rounds, for example, use:

```
python3 run.py bots/sample/ bots/sample/ --max-rounds 500 --save replay.txt
```

There are several provided maps in the *maps/* folder in this scaffold, if you want
to specify which map the game is played on, use the *--map* argument:

```
python3 run.py bots/sample/ bots/sample/ --map circular.map --save replay.txt
```

## Visualizer

To watch a game play out and easily see stats, the blockchain, debug logs and more, 
view your replay files using the visualizer. First, open up *index.html* in the 
*visualizer/* folder in your browser by either double-clicking on the file in file 
explorer, or by running:

```
google-chrome index.html
```

For Windows:

```
start chrome index.html
```

**Commands may vary based on browser**

**Special thanks to @Jay Jayjay for implementing url replay uploads for the visualizer!**

