Include<Array>
Include<Binary>
Include<Boolean>
Include<Conditional>
Include<FloatingPoint>
Include<Function>
Include<Input>
Include<Integer>
Include<Loop>
Include<Output>
Include<String>

ImportStardardModule<Mathematics>
ImportStandardModule<Time>

DefineMain<> [

    Function:CreateLocalFunction<HelloWorld> [
        Output:DisplayAsText<"Hello, World!">
    ]
    
    Function:CreateLocalFunction<Prime> [
        Output:DisplayAsText<Boolean:IsPrime<Input:ReadIntegerFromInput<>>>
    ]

    Function:CreateLocalFunction<Truth> [
        Boolean:DefineVariable<check; Input:ReadIntegerFromInput<>>
        Output:DisplayAsText<check>
        Loop:WhileCondition<check> [
            Output:DisplayAsText<check>
        ]
    ]

    Function:CreateLocalFunction<Cat> [
        Output:DisplayAsText<Input:ReadAllFromInput<>>
    ]

    Function:CreateLocalFunction<Count> [
        Integer:DefineVariable<count; 0>
        Loop:WhileTrue<> [
            Output:DisplayAsText<count>
            Integer:Increment<count>
        ]
    ]

    Function:CreateLocalFunction<All> [
        Integer:DefineVariable<count; 0>
        Output:DisplayAsText<count>
        Loop:WhileTrue<> [
            Integer:Increment<count>
            Loop:Repeat<2; Output:DisplayAsText<count>; Integer:Negate<count>>
        ]
    ]

    Function:CreateLocalFunction<Add> [
        Integer:DefineVariable<a; Input:ReadIntegerFromInput<>>
        Integer:DefineVariable<b; Input:ReadIntegerFromInput<>>
        Output:DisplayAsText<Integer:Sum<a; b>>
    ]

    Function:CreateLocalFunction<Multiply> [
        Integer:DefineVariable<a; Input:ReadIntegerFromInput<>>
        Integer:DefineVariable<b; Input:ReadIntegerFromInput<>>
        Output:DisplayAsText<Integer:Product<a; b>>
    ]

    Function:CreateLocalFunction<RandomOutput> [
        Output:DisplayAsText<FloatingPoint:Random<0; 9>>
    ]

    Function:CreateLocalFunction<InfOutput> [
        Loop:WhileTrue<> [
            Output:DisplayAsText<1>
        ]
    ]

    Function:CreateLocalFunction<InfLoop> [
        Loop:WhileTrue<> [
            Loop:ContinueToNextIteration<>
        ]
    ]

    Function:CreateLocalFunction<Parity> [
        Binary:DefineVariable<a; Input:ReadBinaryByteCharacterFromInput<>>
        Output:DisplayAsText<a:FinalBit<>>
    ]

    Function:CreateLocalFunction<Fibonacci> [
        Mathematics:DefineMathematicalRecursiveFunction<f; n; Integer:Difference<f<Integer:Decrement<n>>; f<Integer:Difference<n; 2>>>>
    ]

    Function:CreateLocalFunction<FizzBuzz> [
        Loop:ForNIterations<N; 1; 100; 1> [
            Conditional:If<Boolean:DivisibleBy<N; 3>> [
                Output:DisplayAsSingleLine<"Fizz">
            ]
            Conditional:ElseIf<Boolean:DivisibleBy<N; 5>> [
                Output:DisplayAsSingleLine<"Buzz">
            ]
            Conditional:Else<> [
                Output:DisplayAsSingleLine<N>
            ]
            Output:DisplayAsText<>
        ]
    ]

    Function:CreateLocalFunction<Divmod> [
        Integer:DefineVariable<a; Input:ReadIntegerFromInput<>>
        Integer:DefineVariable<b; Input:ReadIntegerFromInput<>>
        Output:DisplayAsText<Integer:Quotient<a; b>>
        Output:DisplayAsText<Integer:Modulo<a; b>>
    ]

    Function:CreateLocalFunction<BottlesOfBeer> [
        String:DefineVariable<a; " bottles of beer">
        String:DefineVariable<m; String:Multiline<"{%0%}{%1%} on the wall, {%0%}{%1%}."; "Take one down and pass it around, {%0%}{%1%} on the wall."; "">>
        Loop:ForNIterations<N; 99; 2; Integer:Negate<1>> [
            Output:DisplayAsText<m:Format<N; a>>
        ]
        Output:DisplayAsText<m:RetrieveLine<0>:Format<1; a:WithoutCharacterAtIndex<7>>>
        Output:DisplayAsText<String:Format<"Go to the store and buy some more, 99{%1%}"; a>>
    ]

    Function:CreateLocalFunction<Pause> [
        Integer:DefineVariable<N; 1>
        String:DefineVariable<M; Input:ReadAllFromInput<>>
        Loop:WhileTrue<> [
            Output:DisplayAsText<M>
            Time:PauseForDuration<N>
            Integer:Double<N>
        ]
    ]
]



