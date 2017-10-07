Include<Boolean>
Include<Input>
Include<Integer>
Include<Output>
Include<String>

Structure<Conditional>
Structure<Loop>

String:DefineVariable<program; Input:RetrieveNthARGV<0>>
Integer:DefineVariable<counter; 0>
Loop:ForEachElement<program; char> [
String:DefineVariable<hash; "#">
String:DefineVariable<semi; ";">
Boolean:DefineVariable<ishash; Boolean:ArgumentsAreEqual<char; hash>>
Boolean:DefineVariable<issemi; Boolean:ArgumentsAreEqual<char; semi>>
Conditional:If<ishash> [
String:DefineVariable<output; String:CharacterFromCharCode<counter>>
Output:WriteToSTDOUTWithSpecifiedEnd<output; "">
]
Conditional:If<issemi> [
counter:Increment<>
]
]
