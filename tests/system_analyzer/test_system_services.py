import pytest

from unittest.mock import MagicMock

from src.system_analyzer.core.shell_commands_exec import ShellCommandsExecutor
from src.schemas.system_services import SingleSystemService, ListSystemService
from src.system_analyzer.system_services import SystemServicesCollector


@pytest.fixture
def mock_executor():
    return MagicMock(ShellCommandsExecutor)


def test_collect_services(mock_executor):
    # TODO: Довести до ума тест
    output = "service1 running\nservice2 stopped\nservice3 running"
    mock_executor.return_value.execute.return_value = output

    expected_services = ListSystemService(items=[
        SingleSystemService(name="service1", status="running"),
        SingleSystemService(name="service2", status="stopped"),
        SingleSystemService(name="service3", status="running")
    ])

    collector = SystemServicesCollector()
    collector.executor = mock_executor

    services = collector.collect_services()

    assert services == expected_services
    mock_executor.return_value.execute.assert_called_once_with()


if __name__ == '__main__':
    pytest.main()
