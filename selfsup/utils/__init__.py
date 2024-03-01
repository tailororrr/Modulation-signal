"""The lightly.utils package provides global utility methods.

The io module contains utility to save and load embeddings in a format which is
understood by the Lightly library. With the embeddings_2d module, embeddings
can be transformed to a two-dimensional space for better visualization.

"""

# Copyright (c) 2020. Lightly AG and its affiliates.
# All Rights Reserved

from selfsup.utils.io import save_embeddings
from selfsup.utils.io import load_embeddings
from selfsup.utils.io import check_embeddings
from selfsup.utils.io import load_embeddings_as_dict
from selfsup.utils.io import format_custom_metadata
from selfsup.utils.io import save_custom_metadata
from selfsup.utils.embeddings_2d import fit_pca
from selfsup.utils.benchmarking import BenchmarkModule
from selfsup.utils.benchmarking import knn_predict
