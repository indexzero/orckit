## Model

26. Pin every model: build agents and review CLIs. Record the exact model
    id in `Model:` and the effective window in `Context-window: <integer> tokens`.
    A supported model suffix such as `[1m]` also names the window.
    Record the window's source and the reasoning setting in the ledger.
    An alias such as `opus`, `auto`, or `latest` is not a pin.
    Verify the available window from the host or current provider documentation.
    Never invent a suffix or infer the window from the model family.
    A metadata field records capacity. It does not configure capacity.
    If the required capacity cannot be verified, record BLOCKED.
    Use a transport that can select the model and meet that capacity.
    See SUPERVISOR section 1, Transport. Give each pin a fallback ladder
    and a floor. Tier the model by the defect class the suites cannot see,
    and record the per-item table in the design doc. If a pinned model is
    not available at all, record that in the ledger and BLOCK. Never fall
    back in silence. `checks/model-pinned.sh` checks the declaration format.
    The supervisor verifies availability and capacity at dispatch time.

