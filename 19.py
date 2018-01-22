from util import array, readinput
from re import findall

MOLECULE = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'


def solve(replacements, molecule):
    occurrences = {
        molecule[:i] + rep + molecule[i + len(k):]
        for k, rep in replacements for i in range(len(molecule))
        if molecule[i:i + len(k)] == k
    }
    return len(occurrences)


def solve2(molecule):
    m_elements = molecule.replace('Ar', '|').replace('Rn', '|').replace('Y', ',')
    return len(findall('[A-Z][a-z]*', m_elements)) - m_elements.count(',') - 1


def tests():
    repl = [('H', 'HO'), ('H', 'OH'), ('O', 'HH')]
    assert solve(repl, 'HOH') == 4
    assert solve(repl, 'HOHOHO') == 7
    print('tests pass')


tests()

DATA = [(l[0], l[2]) for l in array(readinput(19))]
print(solve(DATA, MOLECULE))
print(solve2(MOLECULE))
