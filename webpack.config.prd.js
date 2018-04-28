const webpack = require('webpack');
const path = require('path');
const autoprefixer = require('autoprefixer');
const BundleTracker = require('webpack-bundle-tracker');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin')

const source = path.resolve(path.join('./wagtailspace', './static_src'));
const destination = path.resolve(path.join('./wagtailspace', './static'));


process.env['NODE_ENV'] = 'development';

module.exports = {
  entry: {
    'main': [
      'babel-polyfill',
      path.join(source, 'js', 'main.js'),
      path.join(source, 'scss', 'main.scss'),
    ],
  },
  output: {
    path: destination,
    filename: 'bundles/[name]-[hash].js'
  },
  module: {
    rules: [
      { test: /\.js$/, use: 'babel-loader', exclude: /node_modules/ },
      { test: /\.jsx$/, use: 'babel-loader', exclude: /node_modules/ },
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: [
            {
              loader: 'postcss-loader',
              options: {
                plugins: function() {
                  return [autoprefixer({
                    browsers: [
                      'last 2 versions',
                      'safari >= 7'
                    ]
                  })];
                }
              }
            },
            'sass-loader'
          ]
        })
      }
    ],
  },
  resolve: {
    modules: [
      "node_modules"
    ]
  },
  plugins: [
    new ExtractTextPlugin('bundles/[name]-[hash].css'),
    new CopyWebpackPlugin([
      {
        from: path.join(source, 'images'),
        to: path.join(destination, 'images')
      },
    ]),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new UglifyJSPlugin({
      parallel: true,
      uglifyOptions: {
        compress: {
          warnings: false,
          // Disabled because of an issue with Uglify breaking seemingly valid code:
          // https://github.com/facebookincubator/create-react-app/issues/2376
          // Pending further investigation:
          // https://github.com/mishoo/UglifyJS2/issues/2011
          comparisons: false,
        },
        mangle: {
          safari10: true,
        },
        output: {
          comments: false,
          // Turned on because emoji and regex is not minified properly using default
          // https://github.com/facebookincubator/create-react-app/issues/2488
          ascii_only: true,
        }
      }
    }),
    new CleanWebpackPlugin(['wagtailspace/static'], {
      root: process.cwd(),
      verbose: false,
      dry: false,
      watch: false,
    }),
    new BundleTracker({
        filename: './config-prd-stats.json'
    }),
    new webpack.IgnorePlugin(/^\.\/locale$/),
    new webpack.ProvidePlugin({
      $: "jquery",
      jQuery: "jquery",
      'window.jQuery': 'jquery',
      'window.Tether': 'tether',
      tether: 'tether',
      Tether: 'tether',
      Util: "exports-loader?Util!bootstrap/js/dist/util",
      Modal: "exports-loader?Modal!bootstrap/js/dist/modal",
    })
  ]
};
