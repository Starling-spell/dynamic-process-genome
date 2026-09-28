# StudioNet proof ledger

Contract: [0xdd34427ecbA89E43b4e81177AB02416F1e6Cd486](https://explorer-studio.genlayer.com/address/0xdd34427ecbA89E43b4e81177AB02416F1e6Cd486)

All transactions below reached `FINALIZED` with successful leader execution. The deployment, source, and public fixture are pinned to GitHub commit [`09d5ffe`](https://github.com/Starling-spell/dynamic-process-genome/commit/09d5ffe). The SHA-256 of the onchain contract code, that commit's contract file, and the local source was identical: `fb7ceee17772fdb0f36106c44c6b09a80ebdc861cf64aa344b488fc3b2d27a60`.

| Step | Transaction | Observed result |
| --- | --- | --- |
| Deploy | [0x4f260c43…](https://explorer-studio.genlayer.com/tx/0x4f260c43ef76d36a7b14a18aa528edb4ea75713a515c4d95ab5d897729b1a3e6) | Contract created |
| Create space | [0x38fe74f8…](https://explorer-studio.genlayer.com/tx/0x38fe74f8c6a7d0d4ff19328d8d44f3b3acf5546d2ab309843dcb401f01a6b23d) | `demo-process-v1`, version 0 |
| Add input | [0x97d6c012…](https://explorer-studio.genlayer.com/tx/0x97d6c0124b3593b48553a1f6d3dc4a20604b6e0f7fd758beca3dab8217c204be) | Input node stored |
| Add output | [0x77f5b80d…](https://explorer-studio.genlayer.com/tx/0x77f5b80dbdedbbe79ab59edc0182906fd25be1e545ece2edcdcbb4cba3ca5b60) | Output node stored |
| Connect | [0xcfb5a402…](https://explorer-studio.genlayer.com/tx/0xcfb5a4023b8d97b0ed2cbfc61b2d1fc5a827193204b368ce683cb744550784f8) | `input → output` sequence |
| Wrong hash | [0x69736d68…](https://explorer-studio.genlayer.com/tx/0x69736d68e77e02d8cfbdfb05bad51712c838f753e02749c09a0ab241b74a954a) | HTTP 200; actual hash differs from commitment; `INCONCLUSIVE`; version remains 0 |
| Valid mutation | [0x5541341e…](https://explorer-studio.genlayer.com/tx/0x5541341e7c9b9b241f5237450d4dbfbc757a963c9e50c58087081e68a745117e) | Hash match; `SAFE` / `APPLY`; version 1; `input → normalize → output` |

The valid mutation used [`examples/process-spec.txt`](https://github.com/Starling-spell/dynamic-process-genome/blob/09d5ffe/examples/process-spec.txt), fetched from the commit-pinned raw GitHub URL. Its full-response SHA-256 was `2c74ac09218beff2c3eb5ea603beea4cdd0db715cc0c4b417cd9f0745a8a63e1`. The committed report root of the applied mutation is `7072d440e4f9df50b565b9c18a098d90d88b989b1274bcd79faba0519372abcf`. The application receipt records `MAJORITY_AGREE` (three `AGREE`, two `IDLE`), not unanimous agreement.

One earlier attempt with an all-zero hash had GenVM execution `ERROR` because the CLI coerced that argument to an integer. It did not create a proof or change contract state and is intentionally excluded from the table.
