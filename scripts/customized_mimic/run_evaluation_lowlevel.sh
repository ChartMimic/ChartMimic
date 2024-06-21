models=(
  "gpt-4-vision-preview"
)

for model in "${models[@]}"; do
  python chart2code/main.py --cfg eval_configs/customized/code4evaluation.yaml --tasks code4evaluation --model "${model}"
done