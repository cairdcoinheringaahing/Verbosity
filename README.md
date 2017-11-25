# Verbosity
A practical programming language designed to lose code golf competitions

As an example of just how long programs can be, the standard Hello, World! program is 444 bytes long:

    Include<Integer>
    Include<MetaFunctions>
    Include<Output>
    Include<String>

    Integer:DefineVariable<one; 1>
    Output:DefineVariable<STDOUT; 0>
    String:DefineVariable<string; "Hello, World!">

    String:RedefineVariable<string; String:RemoveCharactersFromStart<string; one>>
    String:RedefineVariable<string; String:TakeFirstCharacters<string; one>>

    Output:DisplayAsText<STDOUT; string>

    DefineMain<> [
        MetaFunctions:ExecuteScript<MetaFunctions@FILE>
    ]
