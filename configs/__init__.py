import json
import logging.config
import pathlib


class JsonMessageFormatter(logging.Formatter):
    def format(self, record):
        message_dict = {'message': record.getMessage()}
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        s = self.formatMessage(record)
        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            if s[-1:] != "\n":
                s = s + "\n"
            message_dict['exc_info'] = record.exc_text
        if record.stack_info:
            if s[-1:] != "\n":
                s = s + "\n"
            message_dict['stack_info'] = self.formatStack(record.stack_info)
        return s + json.dumps(message_dict)


def config_log(path=pathlib.Path(__file__).parent / 'log_config.json'):
    with open(path) as f:
        logging.config.dictConfig(json.load(f))
