def pytest_addoption(parser):
    group = parser.getgroup('snapshot')
    group.addoption(
        '--approve',
        action='store_true',
        help='Update snapshot files instead of testing against them.',
    )