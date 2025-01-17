from openood.evaluators.openGan_evaluator import OpenGanEvaluator
from openood.utils import Config

from .base_evaluator import BaseEvaluator
from .draem_evaluator import DRAEMEvaluator
from .fsood_evaluator import FSOODEvaluator
from .kdad_evaluator import KdadDetectionEvaluator
from .ood_evaluator import OODEvaluator


def get_evaluator(config: Config):
    evaluators = {
        'base': BaseEvaluator,
        'ood': OODEvaluator,
        'fsood': FSOODEvaluator,
        'DRAEM': DRAEMEvaluator,
        'openGan': OpenGanEvaluator,
        'kdad': KdadDetectionEvaluator,
    }
    return evaluators[config.evaluator.name](config)
