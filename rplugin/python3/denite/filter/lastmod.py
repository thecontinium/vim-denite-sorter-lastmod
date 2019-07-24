# ============================================================================
# FILE: sorter/lastmod.py
# AUTHOR: The Continium
# DESCRIPTION: Simple filter to sort candidate files by modified time
# License: MIT license
# ============================================================================

import os
from denite.base.filter import Base

class Filter(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter/lastmod'
        self.description = 'sorter for file last modified time'

    def filter(self, context):
        for candidate in context['candidates']:
            candidate['filter__sort'] = os.path.getmtime(
                 candidate['action__path']
            )

        return sorted(
            context['candidates'],
            key=lambda candidate: -candidate['filter__sort']
        )
