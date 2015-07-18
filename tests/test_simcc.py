import nose
import angr
from simuvex.s_cc import SimCCSystemVAMD64

import logging
l = logging.getLogger("angr.tests.test_simcc")

import os
test_location = str(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../binaries/tests'))

def test_simcc_x86_64():
    binary_path = test_location + "/x86_64/simcc"

    p = angr.Project(binary_path)
    cfg = p.analyses.CFG()

    fm = cfg.function_manager

    f_arg1 = fm.function(name='arg1')
    nose.tools.assert_not_equal(f_arg1, None)
    nose.tools.assert_equal(type(f_arg1.cc), SimCCSystemVAMD64)
    nose.tools.assert_equal(len(f_arg1.arguments), 1)
    nose.tools.assert_equal(f_arg1.arguments[0].name, 'rdi')

    f_arg7 = fm.function(name='arg7')
    nose.tools.assert_not_equal(f_arg7, None)
    nose.tools.assert_equal(type(f_arg7.cc), SimCCSystemVAMD64)
    nose.tools.assert_equal(len(f_arg7.arguments), 7)
    nose.tools.assert_equal(f_arg7.arguments[1].name, 'rsi')

    f_arg9 = fm.function(name='arg9')
    nose.tools.assert_not_equal(f_arg9, None)
    nose.tools.assert_equal(type(f_arg9.cc), SimCCSystemVAMD64)
    nose.tools.assert_equal(len(f_arg9.arguments), 9)
    nose.tools.assert_equal(f_arg9.arguments[8].offset, 0x8 + 0x8 * 2)

def run_all():
    functions = globals()
    all_functions = dict(filter((lambda (k, v): k.startswith('test_') and hasattr(v, '__call__')), functions.items()))
    for f in sorted(all_functions.keys()):
        all_functions[f]()

if __name__ == "__main__":
    logging.getLogger("angr.analyses.cfg").setLevel(logging.DEBUG)
    run_all()
