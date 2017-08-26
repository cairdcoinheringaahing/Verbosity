Ignore; `@` is an instance, `:` is a method

Include<Array>
Include<Boolean>
Include<Class>
Include<Conditional>
Include<Dictionary>
Include<Error>
Include<Input>
Include<Integer>
Include<Loop>
Include<Output>
Include<String>

Class:CreateClass<Tape; Array> [
    
    Class:CreateVariableInstance<Tape; tape; Array@Empty@Integer>
    Class:CreateVariableInstance<Tape; index; 0>

    Class:CreateFunctionInstance<MoveLeft> [
        Integer:Decrement<Tape@index>
        Conditional:If<Boolean:LessThan<Tape@index; 0>> [
            Tape@tape:PrependValue<0>
            Integer:Increment<Tape@index>
        ]
    ]

    Class:CreateFunctionInstance<MoveRight> [
        Integer:Increment<Tape@index>
        Conditional:UponErrorFrom<Tape@tape:RetrieveFromIndex<Tape@index>> [
            Tape@tape:AppendValue<0>
        ]
    ]

    Class:CreateFunctionInstance<Increment> [
        Integer:Increment<Tape@tape:RetrieveFromIndex<Tape@index>>
    ]

    Class:CreateFunctionInstance<Decrement> [
        Integer:Decrement<Tape@tape:RetrieveFromIndex<Tape@index>>
    ]

    Class:CreateFunctionInstance<Output> [
        Integer:DefineVariable<c; Tape@tape:RetrieveFromIndex<Tape@index>>
        Output:DisplayAsText<String:ConvertFromCodePoint<c>>
    ]

    Class:CreateFunctionInstance<Input> [
        Tape@tape:DefineValueAtIndex<Tape@index; String:ConvertToCodePoint<Input:ReadCharacterFromInput<>>>
    ]

    Class:CreateFunctionInstance<Commands; char> [
        Dictionary:DefineVariable<commands; Dictionary@Empty>
        commands:DefineKeyItemPair<"+"; Tape:Increment>
        commands:DefineKeyItemPair<"-"; Tape:Decrement>
        commands:DefineKeyItemPair<"<"; Tape:MoveLeft>
        commands:DefineKeyItemPair<">"; Tape:MoveRight>
        commands:DefineKeyItemPair<","; Tape:Input>
        commands:DefineKeyItemPair<"."; Tape:Output>
        Class:ExecuteFunctionInstance<Dictionary:RetrieveValueFromKey<char>>
    ]

]

DefineMain<> [

    String:DefineVariable<program; Input:ReadMultilineFromInput<>>
    Tape:DefineVariable<tape; Tape:Empty>
    Integer:DefineVariable<loop; 0>
    Integer:DefineVariable<bracket; 0>
    String:DefineVariable<char; String@Empty>
    
    Loop:WhileCondition<Boolean:LessThan<loop; Array:Length<program>>> [
        String:RedefineVariable<char; program:RetrieveFromIndex<loop>>
        Conditional:If<Boolean:Equals<char; "[">> [
            Integer:Increment<bracket>
            Conditional:If<Boolean:Not<tape@tape:RetrieveFromIndex<tape@index>>> [
                Integer:RedefineVariable<loop; program:RetrieveLastNFromIndex<"]"; bracket>>
            ]
        ]
        Conditional:If<Boolean:Equals<char; "]">> [
            Conditional:If<Boolean:Evaluate<tape@tape:RetrieveFromIndex<tape@index>>> [
                Integer:RedefineVariable<loop; program:RetrieveFirstNFromIndex<"["; bracket>>
            ]
            Integer:Decrement<bracket>
        ]
        Conditional:UponErrorFrom<tape:Commands<char>> [
            Function:Ignore<>
        ]
        Integer:Increment<loop>
    ]
]
        
