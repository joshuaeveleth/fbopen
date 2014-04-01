from base import AttachmentsBase 

import log
import os
import scrapelib
import sys


class SourceDownloader(AttachmentsBase):
    '''
    This class downloads the opportunity source HTML to support later steps
    of link extraction and download.

    Accepts either a single URL, or a file containing one URL per line.
    '''
    module_name = 'fbo_attach_import.source_downloader'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.urls_file = kwargs.get('file')
        self.resume_url = kwargs.get('resume_url')

        self.req_per_min = 0 # 0 for unlimited


    def run(self):
        self.log.info("Starting: Source Downloader")

        self.grab_urls_from_file()

        self.get_sources()

    def grab_urls_from_file(self):
        if self.urls_file:
            self.log.info("Getting URLs from file {}".format(self.urls_file))
            try:
                with open(self.urls_file, 'r') as f:
                    self.urls = f.readlines()
            except IOError:
                self.log.fatal("Could not open URLs file at path given. Exiting.")
                sys.exit(1)

        else:
            self.log.fatal("URLs file was not provided.")
            sys.exit(1)
       
    def get_sources(self):

        s = scrapelib.Scraper(requests_per_minute=self.req_per_min, follow_robots=False)

        at_resume_point = False
        skipped = 0

        for url in self.urls:
            url = url.strip()
            if (not at_resume_point) and self.resume_url and self.resume_url.strip():
                if url != self.resume_url.strip():
                    skipped += 1
                    continue
                else:
                    at_resume_point = True
                    self.log.info("Resuming. Skipped {} URLs.".format(skipped))

            try:
                filename, response = s.urlretrieve(url, dir=self.import_dir)
                self.log.debug("{} stored at {}".format(url, os.path.basename(filename)))
            except KeyboardInterrupt:
                self._log_resume_info(url)
            except SystemExit:
                self._log_resume_info(url)
            except:
                self.log.exception("Source couldn't be retrieved for {}".format(url))
                continue

    def _log_resume_info(self, url):
        self.log.info("Resume download by adding --resume (-r) flag with last URL logged")
        

if __name__ == '__main__':
    retriever = SourceDownloader(file=sys.argv[1], dir=sys.argv[2])
    retriever.run()