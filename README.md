FBOpen
======

FBOpen is an open API server, data import tools, and sample apps to help small businesses search for opportunities to work with the U.S. government.

The project began as an attempt to make it easier to search the content of [FBO.gov](http://www.fbo.gov), the U.S. government's system of record for opportunities to do business with the government. We downloaded the (XML) data from FBO's weekly data dump of opportunity listings, and loaded it into a [Elasticsearch](http://www.elasticsearch.org) search server. Then we used a primitive crawler to download listings' attachments and load them into Elasticsearch -- something Elasticsearch makes easy thanks to their [Mapper Attachments Type] plugin (https://github.com/elasticsearch/elasticsearch-mapper-attachments).

Underneath the Google-style query page (`/sample-www`), we built a simple REST API (really a thin layer over Elasticsearc's API) so you can build your own query tools.

Then someone realized we didn't have to limit this server to FBO data. There's a second sample data loader that can be used to load data nightly from [grants.gov](http://www.grants.gov), and the API allows you to post opportunities, too.

As of 2014-03-12, we're live at https://fbopen.gsa.gov .

### How to get started
* Clone this repo.
* This repo has an external dependency on another git repo, which needs to be populated at first, so `cd` to the repo and run: `git submodule update --init --recursive`.
* Then install Elasticsearch. FBOpen requires at least version 1.0.0.
* Get the API server up and running. See the README.md in `/api`.
* Load data into the search index using the import tools in `/loaders` -- or roll your own, ~~or use the API's POST `/v0/opp` to post opportunities one at a time~~ (POST functionality is temporarily disabled).
* To run a simple query web page, try the sample app in `/sample-www`.
  * A quick and easy way to access this page at localhost, provided you have Python installed, is to `cd` to the `/sample-www` directory and run: `python -m SimpleHTTPServer`. By default, you'll then be able to access the client at http://localhost:8000

### Examples
* The BusinessUSA PIF team coded up a sample form specifically geared toward submitting or tweaking SBIR solicitations in FBOpen. The relevant code can be found here: [https://github.com/GSA-OCSIT/hyabusa](https://github.com/GSA-OCSIT/hyabusa). Hyabusa is a test-bed Rails 4 app, and includes several other mini-applications, so look for the SbirSolicitationsController and [related views](https://github.com/GSA-OCSIT/hyabusa/tree/master/app/views/sbir_solicitations).
* One of the BusinessUSA PIF's also coded up a sample site to showcase how SBIR.gov could function if FBOpen were the backend data source for the solicitation listings. That repo, as of this writing very much a work in progress, can be found here: [https://github.com/arowla/sbiropen](https://github.com/arowla/sbiropen). This is a Python app built with the Flask microframework.

### Caveat
This project is brand new and very incomplete. No guarantees of data completeness or functionality are implied or should be assumed. There is lots to do!

### Who
FBopen is a joint project of [18F](https://18f.gsa.gov), the [Presidential Innovation Fellowship](http://whitehouse.gov/innovationfellows), and the [GSA](http://www.gsa.gov) [Integrated Award Environment](http://www.gsa.gov/iae).

### License
This project constitutes an original work of the United States Government. This is free and unencumbered software released into the public domain. See the LICENSE file for more.
