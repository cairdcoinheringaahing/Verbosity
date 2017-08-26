 Array

Each Array has a type, that all values must conform to

FUNCTIONS:

- DefineVariable            ->      Empty
    - name: Variable
    - value: Array

- RedefineVariable          ->      Empty
    - name: Variable
    - value: Array

- PrependValue              ->      Array 
    - value: Array@TYPE

- AppendValue               ->      
    - value: Array@TYPE

- InsertAtIndex             ->      
    - index: Integer
    - value: Array@TYPE

- RetrieveFromIndex         ->      
    - index: Integer

- DefineValueAtIndex        ->      
    - index: Integer
    - value: Array@TYPE

- Length                    ->      

- RetrievePreviousFromIndex ->      
    - index: Integer

- RetrieveLastNFromIndex    ->      
    - value: Array@TYPE
    - N: Integer

- RetrieveFirstNFromIndex   ->      
    - value: Array@TYPE
    - N: Integer

- RemoveFirstValue          ->      
    - value: Array@TYPE

- RemoveNValues             ->      
    - value: Array@TYPE
    - N: Integer
    
- RemoveAllValues           ->      
    - value: Array@TYPE

- RemoveValueAtIndex        ->      
    - index: Integer

- TakeSlice                 ->      
    - start: Integer
    - step: Integer
    - end: Integer

- Reverse                   ->      

- SortByKey                 ->      
    - key: Function
    - reverse: Boolean

- ClearAllValues            ->      

- CountInstancesOfValue     ->      
    - value: Array@Type

- Interleave                ->      
    - i_1: Array
    - i_2: Array
    ...
    - i_N: Array

'''
