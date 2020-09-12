# codingclash2020-scaffold

## Engine Installation
To install the engine as a local package, open your [terminal](https://askubuntu.com/questions/38162/what-is-a-terminal-and-how-do-i-open-and-use-it) and run
```
pip install --upgrade codingclash2020
```

(Depending on how your pip is set up, you may need to replace `pip` with `pip3`.) 

## Running

Run a game! Use:

```
python3 run.py bots/sample/ bots/sample/ --save replay.txt
```

You should see the turn numbers outputted to your console as each round ends. 
When the game is over, the replay info will be stored in replay.txt 
(you can use other names for the replay file as well). You can upload the replay file
to the visualizer to watch the game play out.

Place the folder with your own bot code and stubs.py inside the *bots/* folder. If your
folder is named *yourcode/*, for example, you can run a game between the sample bot and 
your bot using 

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