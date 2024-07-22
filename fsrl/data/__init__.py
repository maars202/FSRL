"""Data package."""
# isort:skip_file

from fsrl.data.fast_collector import FastCollector
from fsrl.data.fast_collector_prob import FastCollector as FastCollector_PROB
from fsrl.data.basic_collector import BasicCollector
from fsrl.data.traj_buf import TrajectoryBuffer

__all__ = ["FastCollector", "BasicCollector", "TrajectoryBuffer"]
