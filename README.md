# Abhivyakt

##To start the server on a unix system :
Execute the following command in the terminal
```
#!bash
    ./startApp
```
To populate the database : 

```
    cd scripts
    ./populateDB
``` 

To setup users for the database:
```
#!bash
    ./mongoUserSetup
```


##To start the server on a windows system :
1. Download and install linux
1. Uninstall windows
1. Refer to the above steps

##Development Guidelines:
1. Create a feature/branch for the feature you're building
1. Commit however you want to on the development branch
1. If you've completed coding the feature, raise a pull request
1. Close branch on merge (whoever merges)

##Pull Request Validation Coding Guidelines:
1. Does each function in your code do exactly what it claims to do; neither more nor less?
1. By looking at functions in a file, is it easy to deduce how to use them, and in what context?
1. Are function names intuitive enough such that, if you wanted to do what that function does, you'd be able to search for it without knowing about the function?
1. Are complicated functions broken into smaller simpler operations?
1. Is the code easy to read?
1. Can you DRY your code further?
1. Does DRY-ing this cause any confusion for above points?

###API related
1. Do separate APIs have separate code paths?

##Useful Links
* [Home/Next Meeting Agenda](https://bitbucket.org/atleast3musketeers/hindi/wiki/Home)
* [IDE Recommendations](https://bitbucket.org/atleast3musketeers/hindi/wiki/IDE_Setup)
* [How to Edit The ReadMe](https://bitbucket.org/tutorials/markdowndemo)
