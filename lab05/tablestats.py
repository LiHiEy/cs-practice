def read_rows(lines: list[str]) -> list[dict]:
    header = None
    rows = []
    for line in lines:
        line = line.rstrip("\n").rstrip("\r")
        if not line.strip():
            continue
        parts = [part.strip() for part in line.split(",")]
        if header is None:
            header = parts
            continue
        if len(parts) != len(header):
            continue
        rows.append(dict(zip(header, parts)))
    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row.get("тип", "")
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row.get("тип") != kind:
            continue
        value = row.get("минуты", "").replace(",", ".")
        try:
            total += float(value)
        except ValueError:
            continue
    return round(total, 1)


def to_csv(counts: dict) -> str:
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"