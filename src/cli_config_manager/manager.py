import json
import os
from pathlib import Path


class Config():
    def __init__(self, name):
        self.name = name
        self._config = {}
        self._path = "{}/.{}".format(Path.home(), name)
        self._inital_load = False

    def _read_file(self):
        """Read the config file with the ctor specified name if it exists.
        Will throw exceptions on errors"""
        if self._inital_load is False:
            with open(self._path, "r") as f:
                contents = f.read()
                self._config = json.loads(contents)
        self._inital_load = True

    def load(self):
        """ Load the default profile"""

        self._read_file()

    def load_profile(self, profile) -> (str, map):
        """load profile will load the specified profile. Exceptions will be thrown in the
        event no configuration data is able to be loaded. It will return a tuple with the 
        loaded profile, (will fall back to the config specified default if the passed in
        profile is not in the config file) and the config map"""

        self._read_file()
        try:
            return (profile, self._config[profile])
        except KeyError:
            try:
                return (
                    self._config['default_profile'],
                    self._config[self._config['default_profile']]
                )
            except KeyError:
                raise Exception("Could not retried the specified profile or default profile")
        return ("", {})

    def save_config(self):
        """Save the current config in this class to the config file location"""

        with open(self._path, "w") as f:
            json_config = json.dumps(self._config)
            f.write(json_config)
            os.chmod(self._path, 0o600)

    def add_config(self, config, profile, default_profile=None):
        """Add a new config to this class under the specified profile. Optionally, set his
        config as the default. If this is the first config added, it will be set to default
        reguardless of the the default_profile parameter."""

        # lazy reads
        if self._inital_load is False:
            try:
                self._read_file()
            except Exception:
                pass

        # input sanity check
        if profile is None or profile == "":
            raise Exception("No profile specified")
        if config is None or config == {}:
            raise Exception("No config specified")
        
        if default_profile is None:
            if 'default_profile' not in self._config.keys():
                self._config['default_profile'] = profile
        else:
            self._config['default_profile'] = default_profile
        self._config[profile] = config

    def __write_config(self, config=None, default_profile=None):
        if config is not None:
            self._config = config
        if default_profile is None:
            if 'default_profile' not in self._config.keys():
                for k in self._config.keys():
                    self._config['default_profile'] = k
                    break
        with open(self._path, "w") as f:
            json_config = json.dumps(self._config)
            f.write(json_config)
            os.chmod(self._path, 0o600)

    def get_filepath(self):
        """Return the config file path"""

        return self._path
