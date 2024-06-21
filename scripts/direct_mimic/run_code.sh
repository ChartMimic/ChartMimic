models=(
  "gpt-4-vision-preview"
)

template_type=direct;agent_type=DirectAgent

for model in "${models[@]}"; do
    python chart2code/utils/post_process/code_checker.py \
    --input_file ${PROJECT_PATH}/results/direct/chart2code_${model}_${agent_type}_results.json \
    --template_type ${template_type}
done

for model in "${models[@]}"; do
    python chart2code/utils/post_process/code_interpreter.py \
    --input_file ${PROJECT_PATH}/results/direct/chart2code_${model}_${agent_type}_results.json \
    --template_type ${template_type}
done