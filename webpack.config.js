var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  context: __dirname,

  entry: {
      search: path.resolve('.','assets','src','js','search.js'),
      result: path.resolve('.','assets','src','js','search-result.js')//'.\\assets\\src\\js\\index.js',// entry point of our app. assets/js/index.js should require other js modules and dependencies it needs
  },

  module: {
    rules: [
        { test: /\.css$/, loader: "style-loader!css-loader" },
        { test: /\.scss$/, loader: "style-loader!css-loader!sass-loader" },
        { test: /\.less$/, loader: "style-loader!css-loader!less-loader" },
        {test: /\.(eot|svg|ttf|woff|woff2)$/, loader: 'file-loader?name=fonts/[name].[ext]'}
    ]
  } ,

  output: {
      path: path.resolve('.','assets','bundles'),
      filename: "[name]-[hash].js",
      publicPath: "/static/bundles/",},
  plugins: [
      new BundleTracker({filename: 'webpack-stats.json'}),
      new webpack.NoEmitOnErrorsPlugin(),
  ],


  resolve: {
    modules: ['node_modules'],
    extensions: ['.js', '.css']
  },
}