{
  "targets": [
    {
      "target_name": "shoutjs",
      "actions": [
        {
          "action_name": "run_cmake",
          "inputs": ["CMakeLists.txt"],
          "outputs": ["build/Release/shoutjs.node"],
          "action": ["npx", "cmake-js", "rebuild", "--runtime=electron", "--runtime-version=22.3.27"]
        }
      ]
    }
  ]
}