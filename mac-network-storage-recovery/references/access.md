# Finder SMB access

Distinguish discovery/routing, SMB service negotiation, authentication, share permissions and Finder mounting. A reachable port does not prove any later layer.

Inspect the active network and identified device, then use current supported SMB settings. Prefer the device's exact failure message over guessing that every password prompt means a bad password. Usernames, device passwords and share passwords can differ; use the current vendor/device contract without printing secrets or repeatedly guessing credentials.

After a configuration change or restart, rediscover the device and verify the share afresh. Confirm Finder shows the intended volume, open an existing file without changing it, and verify any requested reconnect behavior. Perform a write test only when the task requires write access and its scope permits a reversible test file. Keep file access separate from Time Machine acceptance.

Report which layer failed or passed. Do not claim the issue is solved merely because a server advertises SMB or a setup tool reports completion.
