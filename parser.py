import re

def flatten(array):
    class ListFlattener(list):
        def push(self,*values):
            for value in values:
                if type(value) in [list, tuple, set]:
                    self.push(*value)
                else:
                    self.append(value)
    flat = ListFlattener()
    flat.push(*array)
    return list(filter(None, list(flat)))

def list_replace(line, old, new):
    if '"' in line:
        example = ''
        strings = ''
        string_toggle = False
        for char in line:
            if char == '"':
                string_toggle ^= 1
            if not string_toggle and char != '"':
                example += char
            else:
                strings += char
                example += '\0'
        example = example.replace(old, new)
        for char in strings:
            example = example.replace('\0', char, 1)
        line = example
    else:
        line = line.replace(old, new)
    return line

def parser(code):
    QUOTE_REGEX = '''((\d+|[A-Za-z@:]+)|("[^"]"))'''
    CMD_REGEX = '''(\[|[, ]){}([,|\]])(\]?, \[)?'''.format(QUOTE_REGEX)
    
    code = list(filter(None, code.strip().replace(' ','').split('\n')))
    for i in range(len(code)):
        if code[i] != ']':
            code[i] = '['+code[i]
        for old, new in [['<', ', ['], ['>', ']'], ['][', '], ['], [';', ', ']]:
            code[i] = list_replace(code[i], old, new)
        if code[i][-1] != '[':
            code[i] += '],'

    parsed = '[\n'

    for l in range(len(code)):
        if code[l] == ']],':
            parsed += ']],\n'
            continue
        matches = re.findall(CMD_REGEX, code[l])

        for m in range(len(matches)):
            matches[m] = list(matches[m])
            matches[m].pop(2)
            if matches[m][2]:
                matches[m].pop(1)
            else:
                matches[m].pop(2)
            for x in range(len(matches[m])):
                if re.search(QUOTE_REGEX, matches[m][x]):
                    matches[m][x] = "'" + matches[m][x] + "'"
            matches[m] = ''.join(matches[m])
        matches = list(map(str.strip, matches))
        line = ' '.join(matches)
        if line == "['DefineMain',":
            line = "['DefineMain', [], ["
        if line[-1] == ',':
            line += ' []'
        if line[-1] != '[':
            line += ']'*(line.count('[')-line.count(']'))+','
        parsed += line + '\n'

    parsed = eval(parsed+']')

    return parsed

print(parser('''Include<Boolean>
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
]'''))
