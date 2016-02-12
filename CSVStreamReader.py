
# The MIT License (MIT)
# Copyright (c) 2016 Chris Webb
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class CSVStreamReader:

    delimiter = '\t'
    text_field_identifier = '"'

    def __init__(self, delimiter, textfieldIdentifier):
        self.delimiter = delimiter
        self.text_field_identifier = textfieldIdentifier

    def getTotalColumns(self, delimiter, textfieldIdentifier, stream, enc):

        curPosition = 0
        if stream.seekable():
            curPosition = stream.tell()
        else:
            return False

        textFieldDelimiterCount = 0
        columnCount = 0
        curChar = stream.read(1)

        while curChar != 0:
            
            if curChar == textfieldIdentifier:
                textFieldDelimiterCount += 1
            elif (textFieldDelimiterCount == 0) or (textFieldDelimiterCount % 2 == 0):
                if curChar == delimiter:
                    columnCount += 1
                elif curChar == '\n':
                    break
            curChar = stream.read(1)

        columnCount += 1
        if stream.seekable():
            stream.seek(curPosition)
        return columnCount

    def readLine (self, stream, startPosition):

        if not startPosition:
            startPosition = 0
        if startPosition >= stream.length:
            return None

        count = 0
        record = []
        curChar = None
        column = 0
        output = []
        endPosition = startPosition
        curChar = stream.read(1)


        while curChar != 0:
            endPosition += 1

            if curChar == textfieldIdentifier:
                if lastChar == curChar:
                    record.append(curChar)
                count += 1
                continue

            elif (count == 0) or (count % 2 == 0):
                if curChar == delimiter:
                    curColumn = column
                    output.push(record.join(""))
                    column += 1
                    record = []
                    continue

                elif curChar == '\r':
                    continue
                elif curChar == '\n':
                    break
            record.push(curChar)
            lastChar = curChar
            curChar = stream.read(1)

        output.push(record.join(""))
        return { "output": output, "endPosition": endPosition }

    def readLines(self, stream):

        pos = 0
        output = []
        returnObj = self.readLine(input, pos)

        while returnObj:
            pos = returnObj.endPosition + 1
            output.push(returnObj.output)

        return output
