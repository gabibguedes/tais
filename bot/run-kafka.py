import logging
import os
import yaml

from rasa_core.utils import configure_colored_logging, read_yaml_file, AvailableEndpoints
from rasa_core.run import start_server, load_agent, start_cmdline_io
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.tracker_store import TrackerStore
from rasa_core.channels.console import CmdlineInput
from rasa_core import constants

logger = logging.getLogger(__name__)
configure_colored_logging(loglevel='DEBUG')

def run(core_dir, nlu_dir):
    _endpoints = AvailableEndpoints.read_endpoints(None)
    _interpreter = NaturalLanguageInterpreter.create(nlu_dir)

    _agent = load_agent(core_dir,
                        interpreter=_interpreter,
                        endpoints=_endpoints)

    http_server = start_server([CmdlineInput()], "", "", 5005, _agent)
    start_cmdline_io(constants.DEFAULT_SERVER_FORMAT.format(5005), http_server.stop)

    try:
        http_server.serve_forever()
    except Exception as exc:
        logger.exception(exc)

if __name__ == '__main__':
    run('models/dialogue', 'models/nlu/current')
