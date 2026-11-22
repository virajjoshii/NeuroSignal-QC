import copy
import uuid
import tempfile
from pathlib import Path
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]

phases = sorted(
    (ROOT / 'notebooks').glob('0[1-5]_*.ipynb')
)

assert len(phases) == 5

combined = nbformat.v4.new_notebook()
combined.nbformat_minor = 5

for path in phases:
    print('Loading:', path.name, flush=True)
    phase = nbformat.read(path, as_version=4)
    nbformat.validate(phase)

    for cell in phase.cells:
        cloned = copy.deepcopy(cell)
        cloned['id'] = uuid.uuid4().hex[:12]

        if cloned.cell_type == 'code':
            cloned.outputs = []
            cloned.execution_count = None

        combined.cells.append(cloned)

nbformat.validate(combined)

with tempfile.TemporaryDirectory(
    prefix='neurosignal_repro_'
) as temp_dir:

    client = NotebookClient(
        combined,
        timeout=1200,
        kernel_name='python3',
        allow_errors=False,
        resources={
            'metadata': {'path': temp_dir}
        }
    )

    client.execute()

print('All five research phases completed.')
