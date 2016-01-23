/*
The MIT License (MIT)
Copyright (c) 2016 Chris Webb
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

var CSVStreamReader = function(delimiter, textfieldIdentifier) {

    if (!textfieldIdentifier)
        textfieldIdentifier = "\"";
    if (!delimiter)
        delimiter = ",";

    this.getTotalColumns = function(input) {

        var textFieldDelimiterCount = 0;
        var columnCount = 0;
        var curChar = undefined;

        for (var i=0; i<input.length; i++) {
            var curChar = input[i];
            
            if (curChar == textfieldIdentifier)
                textFieldDelimiterCount++;
            else if (textFieldDelimiterCount == 0 || textFieldDelimiterCount % 2 == 0) {
                if (curChar == delimiter)
                    columnCount++;
                else if (curChar == '\n')
                    break;
            }
        }

        columnCount++;
        return columnCount;
    }

    var readLine = function(input, startPosition) {

        if (!startPosition)
            startPosition = 0;
        if (startPosition >= input.length)
            return undefined;

        var count = 0;
        var record = [];
        var curChar = undefined;
        var column = 0;
        var output = [];
        var endPosition = startPosition;

        for (var i=startPosition; i<input.length; i++) {
            endPosition = i;
            var lastChar = curChar;
            curChar = input[i];
            if (curChar == textfieldIdentifier) {
                if (lastChar == curChar) {
                    record.push(curChar);
                }
                count++;
                continue;
            }
            else if (count == 0 || count % 2 == 0) {
                if (curChar == delimiter) {
                    var curColumn = column;
                    output.push(record.join(""));
                    column++;
                    record = [];
                    continue;
                }
                else if (curChar == '\r') {
                    continue;
                }
                else if (curChar == '\n') {
                    break;
                }
            }
            record.push(curChar);

        }

        output.push(record.join(""));
        return { output: output, endPosition: endPosition };
    }

    this.readLines = function(input) {

        var i = 0;
        var output = [];
        var returnObj = undefined;

        while (returnObj = readLine(input, i)) {
            i = returnObj.endPosition + 1;
            output.push(returnObj.output);
        }

        return output;
    }

};
