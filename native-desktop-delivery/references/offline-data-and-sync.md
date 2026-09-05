# Offline Data, Portability, And Optional Sync

## Ownership And Recovery

Classify each state item before choosing persistence:

| State | Questions to settle |
| --- | --- |
| Shared business records | Who owns the record, where is it authoritative, and which clients may edit it? |
| Session context | Should independent sessions differ? Should tabs in one session share the selection? |
| Device preferences | Which window, printer, path, and hardware settings must stay on this machine? |
| Credentials | Which values are device-bound, exportable, or require reauthentication after restore? |

Test two devices using the same account. Changing a local preference on one must not silently change the other unless sharing is the agreed behavior. Associate queued work with its original business context rather than whatever workspace is selected later.

Use consistent database snapshots and include required attachments. Validate version/schema, archive integrity, available disk space, and restore compatibility before replacement. Provide a recovery path for interrupted restores. Test with disposable data, retaining original source and user data.

Distinguish a same-device backup from a portable export. Exclude hardware bindings from portable exports or require rebinding; do not copy device-bound ciphertext and claim it will decrypt elsewhere. Verify credentials are either deliberately transferable through the agreed mechanism or explicitly require setup on the destination.

## Synchronization Only When Requested

Before implementing bidirectional sync, settle record identity, ownership, conflict behavior, deletion/tombstones, historical snapshots, and version compatibility. Document unresolved product decisions rather than inventing universal last-write-wins rules.

Design and test durable pending operations, idempotent replay, acknowledgements, cursor advancement, and recovery after crashes. A timeout after a remote write is an uncertain outcome; reconcile before retrying a non-idempotent effect. Test duplicate delivery, out-of-order responses, stale writes, revoked pairing, interrupted reconnection, and a long offline period on the supported database engines.

Keep money and historical documents consistent with their original calculation/version policy. Distinguish syncing business data from syncing device preferences and secrets. Offline support alone does not authorize creating a server synchronization system.
