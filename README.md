# Wterm
Wterm is a simple CLI tool to calculate a reversible and irreversible processes written in Python. It's mainly developed for
thermodinamics testing purposes and it's under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.html) license. 

You must have all these dependencies to run Wterm successfully. 

```shell
$ pip install math argparse 
```

## Basics
We can remember the basic 3 lays of thermodinamics. 
- 1st Law: Energy can't be created or destroyed. It's mainly refered as "the conservation of energy". 
- 2nd Law: The entropy of the universe increases if there's an spontaneous process. 
- 3rd Law: A perfect crystal with 0 K, has cero entropy. 

In thermodinamics, a reversible process is when there's an environment and it's system that can return to the exact state it was or they were in. An irreversible process is the opposite one. It can't be returned to the original state or to the exact states they were in. 

Wterm has an optimization from a previous project with args as keys and values from the CLI using the ```argparse``` library. Project still in development.

## Usage
Soon...


## Local
If you wanna store Wterm in your local, you can type the following commands with [git](https://git-scm.com/).
```shell
$ git clone https://www.github.com/Its-Yayo/Wterm.git
$ cd Wterm
```

If you wanna update all changes of Wterm, you can type the following command.
```shell
$ git pull origin
```

## Pull Requests
First of all, you need to fork and clone the project from your Github's account. You should create a new branch with a name. 
```
$ git checkout -b branch-name
```
Once you make your changes, you should push 'em to your branch.
```
$ git push -u origin branch-name
```
Once the chances are uploaded, you should create a new Pull Request at the top of the page by clicking it. Once you do it, you should compare and review changes from the original and the new branch you created. Finally, you can submit any changes so I can accept/decline any possible implementation. 

## Releases
Soon...

## Notes
This is a special project, since it is modified from a previous assignment I did with a trully special person. 🌷
