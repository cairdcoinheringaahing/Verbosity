Include<Boolean>
Include<Function>
Include<Input>
Include<Integer>
Include<Loop>
Include<Output>
Include<String>

Function:CreateFunction<run; program> [
    Integer:DefineVariable<count; 0>
    Loop:ForEachValue<char; program> [
        Conditional:If<Boolean:Equals<char; ";">> [
            Integer:Increment<count>
        ]
        Conditional:If<Boolean:Equals<char; "#">> [
            Output:DisplayAsText<String:ConvertFromCodePoint<Integer:Modulo<count; 127>>>
            Integer:RedefineVariable<count; 0>
        ]
    ]
    Function:Return<Boolean@Null>
]

DefineMain<> [
    String:DefineVariable<program; Input:ReadMultilineFromInput<>>
    Function:ExecuteFunction<run; program>
]
