# CSVStreamReader
Used to parse delimited strings into a usable structure.
## Installation
To install, add the CSVStreamReader.js file to your DOM via a &lt;script&gt; tag.
## Usage
```js
var reader = new CSVStreamReader(',', '"'); // creates a new stream reader that is comma delimited and text quoted.
var numColumns = reader.getTotalColumns(input); // gets the number of columns from the first row.
var output = reader.readLines(input); // outputs an array from all of the delimited data
```
## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits
This README template was pulled from https://gist.github.com/zenorocha/4526327
## License
MIT License. See LICENSE file.
